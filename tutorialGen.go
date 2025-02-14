package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"math/rand"
	"net/http"
	"os"
	"strings"
	"time"
)

const chatGPTAPIURL = "https://api.openai.com/v1/completions"
const outputDir = "tutorials"
const maxRetries = 3

func main() {
	// Create the output directory if it doesn't exist
	if err := os.MkdirAll(outputDir, os.ModePerm); err != nil {
		fmt.Println("Error creating output directory:", err)
		return
	}

	// Read objectives from file
	objectives, err := ioutil.ReadFile("RHCSA_Objectives.txt")
	if err != nil {
		fmt.Println("Error reading objectives:", err)
		return
	}

	// Split objectives by lines
	lines := strings.Split(string(objectives), "\n")

	// Loop through each objective
	for _, line := range lines {
		if line != "" {
			// Prepare the prompt for ChatGPT API
			prompt := fmt.Sprintf("Please generate in markdown style a tutorial to explain the following Red Hat Certified Systems Administrator Exam 200 Objective: \"%s\" in great depth", line)

			// Call ChatGPT API to generate tutorial with retry mechanism
			tutorial, err := generateTutorialWithRetry(prompt)
			if err != nil {
				fmt.Println("Error generating tutorial:", err)
				continue
			}

			// Generate keywords
			keywords := generateKeywords(tutorial)

			// Create a separate markdown file for each objective
			filename := fmt.Sprintf("%s/%s.md", outputDir, createFilename(line))
			if err := ioutil.WriteFile(filename, []byte(frontMatter(line, keywords)+tutorial), os.ModePerm); err != nil {
				fmt.Println("Error writing to file:", err)
				continue
			}
			fmt.Println("Tutorial for", line, "written to", filename)
		}
	}

	fmt.Println("Tutorials generated and written to", outputDir)
}

func generateTutorialWithRetry(prompt string) (string, error) {
	for retry := 0; retry < maxRetries; retry++ {
		tutorial, err := generateTutorial(prompt)
		if err != nil {
			fmt.Println("Error generating tutorial:", err)
			continue
		}
		return tutorial, nil
	}
	return "", fmt.Errorf("maximum number of retries reached, unable to generate tutorial")
}

func generateTutorial(prompt string) (string, error) {
	// Construct request payload
	requestData := map[string]interface{}{
		"prompt":     prompt,
		"max_tokens": 500,
		"model":      "gpt-3.5-turbo-instruct",
	}
	requestBody, err := json.Marshal(requestData)
	if err != nil {
		return "", err
	}

	// Create HTTP request
	req, err := http.NewRequest("POST", chatGPTAPIURL, bytes.NewBuffer(requestBody))
	if err != nil {
		return "", err
	}
	apiKey := os.Getenv("API_KEY")
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	// Read response body
	responseBody, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	// Extract the 'text' field from the response
	var jsonResponse map[string]interface{}
	err = json.Unmarshal(responseBody, &jsonResponse)
	if err != nil {
		return "", err
	}

	choices, ok := jsonResponse["choices"].([]interface{})
	if !ok || len(choices) == 0 {
		return "", fmt.Errorf("no choices found in response")
	}

	text, ok := choices[0].(map[string]interface{})["text"].(string)
	if !ok {
		return "", fmt.Errorf("error extracting 'text' field from response")
	}

	return text, nil
}

func createFilename(objective string) string {
	// Replace spaces, apostrophes, and commas with underscores
	filename := strings.ReplaceAll(objective, " ", "_")
	filename = strings.ReplaceAll(filename, "'", "")
	filename = strings.ReplaceAll(filename, ",", "")
	return filename
}

func frontMatter(title, keywords string) string {
	// Prepare front matter with title and keywords
	return fmt.Sprintf(`+++
title = "%s"
date = "%s"
author = "root"
cover = ""
tags = [%s]
keywords = [%s]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++
`, title, time.Now().Format(time.RFC3339), keywords, keywords)
}

func generateKeywords(text string) string {
	// Split the text into words
	words := strings.Fields(text)

	// Use a map to store unique words
	wordMap := make(map[string]bool)

	// Add words to the map
	for _, word := range words {
		// Convert word to lowercase to ensure uniqueness
		word = strings.ToLower(word)
		wordMap[word] = true
	}

	// Convert the map keys to a slice
	var uniqueWords []string
	for word := range wordMap {
		uniqueWords = append(uniqueWords, word)
	}

	// Shuffle the slice of unique words
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(uniqueWords), func(i, j int) {
		uniqueWords[i], uniqueWords[j] = uniqueWords[j], uniqueWords[i]
	})

	// Ensure we have at least 8 keywords
	minKeywords := 8
	if len(uniqueWords) < minKeywords {
		duplicates := minKeywords / len(uniqueWords)
		remainder := minKeywords % len(uniqueWords)

		// Duplicate the words
		for i := 0; i < duplicates; i++ {
			uniqueWords = append(uniqueWords, uniqueWords...)
		}

		// Add the remainder of unique words
		uniqueWords = append(uniqueWords, uniqueWords[:remainder]...)
	}

	// Trim the slice to contain only 8 keywords
	uniqueWords = uniqueWords[:minKeywords]

	// Convert keywords to string slice
	keywordStrings := make([]string, len(uniqueWords))
	for i, keyword := range uniqueWords {
		keywordStrings[i] = `"` + keyword + `"`
	}

	// Convert keyword strings to string slice
	return "[" + strings.Join(keywordStrings, ", ") + "]"
}
