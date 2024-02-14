package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

const (
	chatGPTAPIURL = "https://api.openai.com/v1/completions"
	outputFile    = "tutorials.md"
)

func main() {
	// Open the output file for writing
	file, err := os.Create(outputFile)
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close()

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
			prompt := fmt.Sprintf("{%s}: ", line)

			// Call ChatGPT API to generate tutorial
			tutorial, err := generateTutorial(prompt)
			if err != nil {
				fmt.Println("Error generating tutorial:", err)
				continue
			}

			// Write the generated tutorial to the file
			_, err = file.WriteString("## " + line + "\n\n" + tutorial + "\n\n")
			if err != nil {
				fmt.Println("Error writing to file:", err)
				continue
			}
		}
	}

	fmt.Println("Tutorials generated and written to", outputFile)
}

func generateTutorial(prompt string) (string, error) {
	// You need to replace "YOUR_API_KEY" with your actual OpenAI API key
	req, err := http.NewRequest("POST", chatGPTAPIURL, strings.NewReader(`{"prompt": "`+prompt+`", "max_tokens": 500}`))
	if err != nil {
		return "", err
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer YOUR_API_KEY")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}