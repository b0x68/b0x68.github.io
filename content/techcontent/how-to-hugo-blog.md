+++
title = "Beginner: Start a Blog with HUGO"
date = "2022-12-16"
author = "Admin"
authorTwitter = "hrklib" #do not include @
cover = "hugo-logo-wide.svg"
tags = ["hugo", "blog", "go", "programming", "web development"]
keywords = ["hugo", "blog", "go", "programming", "web development"]
description = "Hi! I'm brand new to HUGO and this is my version of 'how to' with HUGO as a complete beginner. Follow along to start _your_ very own blog." 
showFullContent = false
readingTime = false
hideComments = false
color = "" #color from the theme settings
+++

I'm brand new to HUGO and this is my version of 'how to with HUGO as a beginner'. My first post will be a walk through of how I went about spinning up this site.

# _What_ is HUGO?

> TLDR: _Hugo is a fast and modern static site generator written in Go, and designed to make website creation fun again_.

If you really want to learn about HUGO, you should [head on over to their official site.](https://gohugo.io/about/what-is-hugo/)

I can confirm; HUGO makes _learning_ website creation bearable. Admittedly, I'm not very interested in the low-level intricacies of front end languages, so using HUGO, where there are many fully-fledged themes freely available and the integration of [markdown](https://www.markdownguide.org/getting-started/), makes this type of project _fun_ and easy :) Understandably, your definition of fun may vary! 

I acknowledge some custom HTML, CSS, and/or Javascript work will need to be done if you're not completely satisfied with your theme's look and feel. A future post, perhaps.

---
# My Environment
  * MacOS Ventura 13.0
  * Go(lang) version go1.19.4 darwin/amd64
  * Hugo v0.108.0+extended darwin/amd64

  Keep in mind, there are many options for what your environment can be, e.g., Docker, Vagrant, a VM, Cloud based, etc. These are outside the scope of this article, but you can easily web search this information and choose your desired setup.
* Software
  * [Hugo](https://gohugo.io/installation/) - **`required`**
  * [Git](https://github.com/git-guides/install-git) - **`required`**
  * Text Editor ([vim](https://www.vim.org/download.php), [VSCode](https://code.visualstudio.com/download), etc.) - **`required`**
  * [Go](https://go.dev/doc/install) - _`recommended`_
---
# Let's Begin

Okay, so first, I make a dev environment in my `~/projects/` directory.

```bash
mkdir ~/projects/hugo

hugo new site blog-dev

cd blog-dev

# git init for later when we push to github
git init

git submodule add https://github.com/panr/hugo-theme-terminal themes/terminal

# edit line "theme = 'terminal'" in editor \
# of your choice. Mine is vim
vim config.toml

# now let's test to make sure it's working
hugo server --port 1313
```

```terminal
# sample output of local webserver on successful startup

Start building sites …
hugo v0.108.0+extended darwin/amd64 BuildDate=unknown

                   | EN
-------------------+-----
  Pages            | 38
  Paginator pages  |  0
  Non-page files   |  0
  Static files     | 11
  Processed images |  0
  Aliases          | 15
  Sitemaps         |  1
  Cleaned          |  0

Built in 58 ms
Watching for changes in /Users/bh19/projects/hugo/hrklib/{archetypes,assets,content,data,layouts,static,themes}
Watching for config changes in /Users/bh19/projects/hugo/hrklib/config.toml, /Users/bh19/projects/hugo/hrklib/themes/terminal/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Now, open an incognito web browser window and navigate the [http://localhost:1313/](http://localhost:1313/)

You should see bare bones Terminal themed website. Like below

![screenshot](pic.png)



