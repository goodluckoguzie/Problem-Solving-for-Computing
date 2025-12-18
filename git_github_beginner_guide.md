# Git & GitHub: Complete Beginner's Guide

---

## Summary
This guide provides a **complete introduction to Git and GitHub** for beginners. You'll learn what Git is, how it works, and how to use it for version control. We'll cover everything from basic concepts to creating repositories, making commits, working with branches, and collaborating on GitHub. Each concept includes clear definitions, explanations, and practical examples.

### Key Terms & Definitions (Glossary)
- **Git:** A **distributed version control system** that tracks changes in files and coordinates work among multiple people.
- **GitHub:** A **cloud-based hosting service** for Git repositories that provides a web interface and collaboration features.
- **Repository (Repo):** A **folder or directory** that contains your project files and the entire history of changes tracked by Git.
- **Commit:** A **snapshot** of your project at a specific point in time. It saves your changes with a message describing what was changed.
- **Branch:** A **parallel version** of your repository that allows you to work on features without affecting the main code.
- **Merge:** The process of **combining changes** from one branch into another.
- **Push:** **Uploading** your local commits to a remote repository (like GitHub).
- **Pull:** **Downloading** changes from a remote repository to your local repository.
- **Clone:** **Copying** an entire repository from GitHub to your local computer.
- **Fork:** Creating a **personal copy** of someone else's repository on GitHub.
- **Pull Request (PR):** A **request to merge** changes from one branch into another, often used for code review.
- **Staging Area:** An **intermediate area** where you prepare changes before committing them.
- **Working Directory:** Your **current project folder** where you make changes to files.
- **Remote:** A **reference to a repository** hosted on GitHub or another server.
- **HEAD:** A **pointer** to the current branch and commit you're working on.
- **Origin:** The **default name** for the remote repository (usually your GitHub repo).

---

## Table of Contents
1. Introduction: What is Git and Why Use It?
2. Installing Git
3. Initial Setup: Configuring Git
4. Understanding How Git Works
5. Creating Your First Repository
6. Basic Git Workflow
7. Making Your First Commit
8. Viewing History and Changes
9. Working with Branches
10. Merging Branches
11. Connecting to GitHub
12. Pushing to GitHub
13. Pulling from GitHub
14. Cloning a Repository
15. Working with Remote Repositories
16. Undoing Changes
17. Common Git Commands Reference
18. Best Practices
19. Troubleshooting Common Issues
20. Practice Exercises

---

# 1) Introduction: What is Git and Why Use It?

### What is Version Control?
**Version control** is a system that records changes to files over time, allowing you to:
- **Track changes** in your code
- **Go back** to previous versions
- **Collaborate** with others without conflicts
- **See who** made what changes and when

### What is Git?
**Git** is a free, open-source **distributed version control system** created by Linus Torvalds (creator of Linux). It's designed to:
- Handle projects of any size efficiently
- Work offline (you don't need internet for most operations)
- Support non-linear workflows (branches, merges)
- Be fast and reliable

### What is GitHub?
**GitHub** is a cloud-based hosting service for Git repositories. It provides:
- **Web interface** to view and manage repositories
- **Collaboration tools** (pull requests, issues, discussions)
- **Free hosting** for public repositories
- **Backup** of your code in the cloud

### Why Use Git?
1. **Backup:** Your code is saved in multiple places
2. **History:** See every change you've ever made
3. **Collaboration:** Multiple people can work on the same project
4. **Experimentation:** Try new features without breaking working code
5. **Recovery:** Easily undo mistakes and restore previous versions

---

# 2) Installing Git

### Windows
1. Download Git from: https://git-scm.com/download/win
2. Run the installer
3. Use default settings (recommended for beginners)
4. Open **Git Bash** or **Command Prompt** to verify:
   ```bash
   git --version
   ```
   Should display: `git version 2.x.x`

### Mac
```bash
# Using Homebrew (if installed)
brew install git

# Or download from: https://git-scm.com/download/mac
```

### Linux
```bash
# Ubuntu/Debian
sudo apt-get install git

# Fedora
sudo dnf install git
```

### Verify Installation
```bash
git --version
```

---

# 3) Initial Setup: Configuring Git

Before using Git, you need to tell it who you are:

### Set Your Name
```bash
git config --global user.name "Your Name"
```
**Example:**
```bash
git config --global user.name "John Doe"
```

### Set Your Email
```bash
git config --global user.email "your.email@example.com"
```
**Example:**
```bash
git config --global user.email "john.doe@example.com"
```

### Verify Configuration
```bash
git config --global --list
```

**Output:**
```
user.name=John Doe
user.email=john.doe@example.com
```

### Explanation
- `--global` means these settings apply to **all repositories** on your computer
- Use the **same email** as your GitHub account
- You can override these settings per repository if needed

---

# 4) Understanding How Git Works

### The Three States of Git

Git has three main areas where your files can exist:

1. **Working Directory** (Your Files)
   - Where you **edit files** normally
   - Files you see in your folder
   - Changes here are **not tracked** yet

2. **Staging Area** (Index)
   - **Prepared changes** ready to be committed
   - Files you've marked to be included in the next commit
   - Think of it as a **shopping cart** before checkout

3. **Repository** (Git History)
   - **Committed snapshots** of your project
   - Permanent record of all changes
   - Stored in the `.git` folder

### Visual Representation
```
Working Directory → (git add) → Staging Area → (git commit) → Repository
     (Edit files)                    (Prepare)              (Save snapshot)
```

### The Basic Workflow
1. **Edit files** in your working directory
2. **Stage changes** using `git add` (move to staging area)
3. **Commit changes** using `git commit` (save to repository)

---

# 5) Creating Your First Repository

### Method 1: Initialize a New Repository Locally

**Step 1:** Create a project folder
```bash
# Windows
mkdir my-first-project
cd my-first-project

# Mac/Linux
mkdir my-first-project
cd my-first-project
```

**Step 2:** Initialize Git
```bash
git init
```

**Output:**
```
Initialized empty Git repository in /path/to/my-first-project/.git/
```

**What happened?**
- Git created a hidden `.git` folder
- This folder contains all Git history and configuration
- Your folder is now a Git repository!

**Step 3:** Create a file
```bash
# Create a simple text file
echo "Hello, Git!" > hello.txt
```

**Step 4:** Check status
```bash
git status
```

**Output:**
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.txt

nothing added to commit but untracked files present
```

### Method 2: Clone an Existing Repository

```bash
git clone https://github.com/username/repository-name.git
```

**Example:**
```bash
git clone https://github.com/goodluckoguzie/Problem-Solving-for-Computing.git
```

This creates a folder with the repository name and downloads all files and history.

---

# 6) Basic Git Workflow

The basic Git workflow consists of three main steps:

### Step 1: Make Changes
Edit, create, or delete files in your working directory.

**Example:**
```bash
# Create a new file
echo "# My Project" > README.md

# Or edit an existing file using your text editor
```

### Step 2: Stage Changes (`git add`)
Tell Git which changes you want to include in the next commit.

```bash
# Stage a specific file
git add filename.txt

# Stage all files in current directory
git add .

# Stage all files in entire project
git add -A

# Stage multiple specific files
git add file1.txt file2.txt
```

**Example:**
```bash
git add README.md
git status
```

**Output:**
```
On branch main
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
        new file:   README.md
```

### Step 3: Commit Changes (`git commit`)
Save your staged changes with a descriptive message.

```bash
git commit -m "Your commit message"
```

**Example:**
```bash
git commit -m "Add README file"
```

**Output:**
```
[main (root-commit) abc1234] Add README file
 1 file changed, 1 insertion(+)
```

### Complete Example Workflow

```bash
# 1. Create a new file
echo "print('Hello, World!')" > hello.py

# 2. Check status
git status
# Shows: hello.py is untracked

# 3. Stage the file
git add hello.py

# 4. Check status again
git status
# Shows: hello.py is staged and ready to commit

# 5. Commit the change
git commit -m "Add hello.py program"

# 6. Check status
git status
# Shows: nothing to commit, working tree clean
```

---

# 7) Making Your First Commit

### Understanding Commits

A **commit** is a snapshot of your project at a specific moment. Each commit has:
- **Unique ID** (hash) - e.g., `abc1234def5678`
- **Author** - Your name and email
- **Date/Time** - When it was created
- **Message** - Description of what changed
- **Parent commit** - Link to previous commit

### Writing Good Commit Messages

**Good commit messages:**
- Are **clear and descriptive**
- Use **imperative mood** ("Add feature" not "Added feature")
- Are **concise** but informative
- Explain **what** and **why**, not how

**Examples:**
```bash
# Good
git commit -m "Add user login functionality"
git commit -m "Fix bug in calculation function"
git commit -m "Update README with installation instructions"

# Bad
git commit -m "changes"
git commit -m "fixed stuff"
git commit -m "asdfghjkl"
```

### Making Multiple Commits

```bash
# First commit
echo "# Project Title" > README.md
git add README.md
git commit -m "Add README file"

# Second commit
echo "print('Hello')" > main.py
git add main.py
git commit -m "Add main Python script"

# Third commit
echo "Version 1.0" >> README.md
git add README.md
git commit -m "Update README with version number"
```

### Viewing Your Commits

```bash
# View commit history
git log

# View in one line per commit
git log --oneline

# View with graph
git log --oneline --graph
```

**Example Output:**
```
abc1234 (HEAD -> main) Update README with version number
def5678 Add main Python script
ghi9012 Add README file
```

---

# 8) Viewing History and Changes

### View Commit History

```bash
# Full history with details
git log

# One line per commit
git log --oneline

# Last 5 commits
git log -5

# With graph visualization
git log --oneline --graph --all
```

### View Changes in Files

```bash
# See what changed (unstaged changes)
git diff

# See what's staged
git diff --staged

# See changes in a specific file
git diff filename.txt

# See changes in a specific commit
git show abc1234
```

### View Current Status

```bash
git status
```

**Shows:**
- Which files are modified
- Which files are staged
- Which files are untracked
- Current branch name

**Example Output:**
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
        modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        newfile.txt

no changes added to commit (use "git add" to stage and/or "git commit" to commit)
```

---

# 9) Working with Branches

### What is a Branch?

A **branch** is a parallel version of your repository. Think of it as:
- A **separate timeline** for your project
- A way to work on features **without affecting** the main code
- A **safe space** to experiment

### Why Use Branches?

1. **Work on features** without breaking main code
2. **Experiment** safely
3. **Collaborate** with others
4. **Organize** your work

### Creating and Switching Branches

```bash
# Create a new branch
git branch feature-name

# Switch to a branch
git checkout feature-name

# Create and switch in one command
git checkout -b feature-name

# Or using newer syntax
git switch -c feature-name
```

**Example:**
```bash
# Create and switch to a new branch
git checkout -b add-login-feature

# Make changes
echo "def login():" > login.py
git add login.py
git commit -m "Add login function"

# Switch back to main
git checkout main
```

### Listing Branches

```bash
# List local branches
git branch

# List all branches (including remote)
git branch -a

# List remote branches
git branch -r
```

**Example Output:**
```
  add-login-feature
* main
  update-ui
```
The `*` shows your current branch.

### Deleting Branches

```bash
# Delete a branch (must be on a different branch)
git branch -d branch-name

# Force delete (even if not merged)
git branch -D branch-name
```

---

# 10) Merging Branches

### What is Merging?

**Merging** combines changes from one branch into another. It's how you bring your feature work back into the main branch.

### Basic Merge Process

**Step 1:** Switch to the branch you want to merge INTO
```bash
git checkout main
```

**Step 2:** Merge the feature branch
```bash
git merge feature-name
```

**Step 3:** Resolve conflicts (if any)
```bash
# Git will tell you if there are conflicts
# Edit the conflicted files, then:
git add conflicted-file.txt
git commit -m "Merge feature-name into main"
```

### Complete Merge Example

```bash
# Start on main branch
git checkout main

# Create a new feature branch
git checkout -b add-calculator

# Make changes on feature branch
echo "def add(a, b): return a + b" > calculator.py
git add calculator.py
git commit -m "Add calculator function"

# Switch back to main
git checkout main

# Merge the feature branch
git merge add-calculator
```

**Output:**
```
Updating abc1234..def5678
Fast-forward
 calculator.py | 1 +
 1 file changed, 1 insertion(+)
```

### Merge Conflicts

Sometimes Git can't automatically merge changes. This creates a **conflict**.

**Example Conflict:**
```
<<<<<<< HEAD
print("Hello from main")
=======
print("Hello from feature")
>>>>>>> feature-branch
```

**How to Resolve:**
1. Open the conflicted file
2. Choose which version to keep (or combine both)
3. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Stage the resolved file: `git add filename.txt`
5. Complete the merge: `git commit`

---

# 11) Connecting to GitHub

### Create a GitHub Account

1. Go to https://github.com
2. Sign up for a free account
3. Verify your email

### Create a Repository on GitHub

1. Click the **"+"** icon → **"New repository"**
2. Enter repository name (e.g., `my-first-project`)
3. Choose **Public** or **Private**
4. **Don't** initialize with README (if you already have local files)
5. Click **"Create repository"**

### Connect Local Repository to GitHub

**Step 1:** Get your repository URL from GitHub
- Click the green **"Code"** button
- Copy the HTTPS URL (e.g., `https://github.com/username/repo-name.git`)

**Step 2:** Add remote to your local repository
```bash
git remote add origin https://github.com/username/repo-name.git
```

**Step 3:** Verify the remote
```bash
git remote -v
```

**Output:**
```
origin  https://github.com/username/repo-name.git (fetch)
origin  https://github.com/username/repo-name.git (push)
```

### Understanding Remotes

- **Remote:** A reference to a repository hosted elsewhere
- **Origin:** The default name for your main remote repository
- You can have multiple remotes (origin, upstream, etc.)

---

# 12) Pushing to GitHub

### What is Pushing?

**Pushing** uploads your local commits to a remote repository (like GitHub).

### First Push (Setting Upstream)

```bash
# Push and set upstream branch
git push -u origin main
```

**Explanation:**
- `push` - Upload commits
- `-u` - Set upstream (tracking) branch
- `origin` - Remote repository name
- `main` - Branch to push

**Example:**
```bash
git push -u origin main
```

**Output:**
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 450 bytes | 450.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/username/repo-name.git
 * [new branch]      main -> main
Branch 'main' set up to track 'origin/main'.
```

### Subsequent Pushes

After the first push, you can simply use:
```bash
git push
```

### Pushing a Specific Branch

```bash
# Push a specific branch
git push origin branch-name

# Push all branches
git push --all origin
```

### Authentication

When pushing, GitHub will ask for authentication:

**Option 1: Personal Access Token (Recommended)**
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo`
4. Copy the token
5. Use token as password when pushing

**Option 2: SSH Keys (Advanced)**
Set up SSH keys for passwordless authentication.

---

# 13) Pulling from GitHub

### What is Pulling?

**Pulling** downloads changes from a remote repository and merges them into your local repository.

### Basic Pull

```bash
# Pull latest changes
git pull

# Or specify remote and branch
git pull origin main
```

### Pull Process

`git pull` is actually two commands combined:
1. `git fetch` - Downloads changes
2. `git merge` - Merges them into your branch

### Example Scenario

**Situation:** Someone else (or you on another computer) pushed changes to GitHub.

```bash
# Check what's on remote
git fetch origin

# See the difference
git log HEAD..origin/main

# Pull the changes
git pull origin main
```

**Output:**
```
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/username/repo-name
   abc1234..def5678  main       -> origin/main
Updating abc1234..def5678
Fast-forward
 newfile.txt | 1 +
 1 file changed, 1 insertion(+)
```

### Handling Pull Conflicts

If local and remote changes conflict:

```bash
git pull origin main
# Git will tell you about conflicts

# Resolve conflicts in files
# Then:
git add resolved-file.txt
git commit -m "Merge remote changes"
```

---

# 14) Cloning a Repository

### What is Cloning?

**Cloning** creates a complete copy of a remote repository on your local computer, including all history and branches.

### Clone a Repository

```bash
git clone https://github.com/username/repository-name.git
```

**Example:**
```bash
git clone https://github.com/goodluckoguzie/Problem-Solving-for-Computing.git
```

This creates a folder named `Problem-Solving-for-Computing` with all files.

### Clone to a Specific Folder

```bash
git clone https://github.com/username/repo-name.git my-folder-name
```

### Clone a Specific Branch

```bash
git clone -b branch-name https://github.com/username/repo-name.git
```

### What Happens When You Clone?

1. Creates a new folder
2. Downloads all files
3. Downloads complete history
4. Sets up remote tracking
5. Checks out the default branch (usually `main`)

### After Cloning

```bash
# Navigate into the cloned repository
cd repository-name

# Check status
git status

# View remotes
git remote -v
```

---

# 15) Working with Remote Repositories

### Viewing Remotes

```bash
# List all remotes
git remote

# List with URLs
git remote -v
```

### Adding a Remote

```bash
git remote add remote-name https://github.com/username/repo.git
```

**Example:**
```bash
git remote add upstream https://github.com/original-author/repo.git
```

### Removing a Remote

```bash
git remote remove remote-name
```

### Renaming a Remote

```bash
git remote rename old-name new-name
```

### Fetching from Remote

```bash
# Download changes without merging
git fetch origin

# Fetch from specific remote
git fetch upstream

# Fetch all remotes
git fetch --all
```

### Viewing Remote Branches

```bash
# List remote branches
git branch -r

# List all branches (local and remote)
git branch -a
```

---

# 16) Undoing Changes

### Undo Unstaged Changes

**Discard changes in a file:**
```bash
git checkout -- filename.txt
# Or newer syntax:
git restore filename.txt
```

**Discard all unstaged changes:**
```bash
git checkout -- .
# Or:
git restore .
```

### Unstage Files

**Unstage a specific file:**
```bash
git reset HEAD filename.txt
# Or newer syntax:
git restore --staged filename.txt
```

**Unstage all files:**
```bash
git reset HEAD
```

### Undo Last Commit (Keep Changes)

```bash
# Undo commit but keep changes staged
git reset --soft HEAD~1

# Undo commit and unstage changes (keep files)
git reset HEAD~1
# or
git reset --mixed HEAD~1
```

### Undo Last Commit (Discard Changes)

```bash
# ⚠️ WARNING: This permanently deletes changes
git reset --hard HEAD~1
```

### Amend Last Commit

**Change the last commit message:**
```bash
git commit --amend -m "New commit message"
```

**Add more changes to last commit:**
```bash
git add forgotten-file.txt
git commit --amend --no-edit
```

### Revert a Commit

**Create a new commit that undoes a previous commit:**
```bash
git revert commit-hash
```

**Example:**
```bash
git revert abc1234
```

This is safer than `reset` because it doesn't rewrite history.

---

# 17) Common Git Commands Reference

### Essential Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `git init` | Initialize repository | `git init` |
| `git status` | Check status | `git status` |
| `git add` | Stage changes | `git add file.txt` |
| `git commit` | Save changes | `git commit -m "message"` |
| `git log` | View history | `git log --oneline` |
| `git diff` | View changes | `git diff` |
| `git push` | Upload to remote | `git push origin main` |
| `git pull` | Download from remote | `git pull origin main` |
| `git clone` | Copy repository | `git clone <url>` |

### Branch Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `git branch` | List branches | `git branch` |
| `git branch name` | Create branch | `git branch feature` |
| `git checkout name` | Switch branch | `git checkout feature` |
| `git checkout -b name` | Create & switch | `git checkout -b feature` |
| `git merge name` | Merge branch | `git merge feature` |
| `git branch -d name` | Delete branch | `git branch -d feature` |

### Remote Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `git remote` | List remotes | `git remote` |
| `git remote -v` | List with URLs | `git remote -v` |
| `git remote add` | Add remote | `git remote add origin <url>` |
| `git remote remove` | Remove remote | `git remote remove origin` |
| `git fetch` | Download changes | `git fetch origin` |

### Information Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `git show` | Show commit | `git show abc1234` |
| `git log` | View history | `git log --oneline` |
| `git diff` | View changes | `git diff` |
| `git status` | Check status | `git status` |
| `git branch -a` | All branches | `git branch -a` |

---

# 18) Best Practices

### Commit Best Practices

1. **Commit often** - Small, frequent commits are better than large ones
2. **Write clear messages** - Describe what and why, not how
3. **One logical change per commit** - Don't mix unrelated changes
4. **Test before committing** - Make sure code works

**Good commit messages:**
```
✅ "Add user authentication"
✅ "Fix calculation bug in tax function"
✅ "Update README with installation steps"
```

**Bad commit messages:**
```
❌ "changes"
❌ "fixed stuff"
❌ "asdf"
❌ "WIP"
```

### Branch Best Practices

1. **Use descriptive names** - `add-login-feature` not `branch1`
2. **Keep main stable** - Only merge tested, working code
3. **Delete merged branches** - Clean up after merging
4. **One feature per branch** - Don't mix multiple features

**Good branch names:**
```
✅ feature/user-login
✅ bugfix/calculation-error
✅ update/readme-documentation
```

**Bad branch names:**
```
❌ branch1
❌ test
❌ new-stuff
```

### Workflow Best Practices

1. **Pull before push** - Always pull latest changes first
2. **Review before commit** - Use `git status` and `git diff`
3. **Don't commit sensitive data** - No passwords, API keys, etc.
4. **Use .gitignore** - Exclude unnecessary files

### .gitignore File

Create a `.gitignore` file to exclude files from Git:

**Example .gitignore:**
```
# Python
__pycache__/
*.py[cod]
*.pyc
venv/
env/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Environment variables
.env
.env.local
```

---

# 19) Troubleshooting Common Issues

### Issue: "fatal: not a git repository"

**Problem:** You're not in a Git repository.

**Solution:**
```bash
# Make sure you're in the right directory
cd /path/to/your/project

# Or initialize a new repository
git init
```

### Issue: "Please tell me who you are"

**Problem:** Git doesn't know your identity.

**Solution:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Issue: "Updates were rejected because the remote contains work"

**Problem:** Remote has changes you don't have locally.

**Solution:**
```bash
# Pull first, then push
git pull origin main
git push origin main
```

### Issue: Merge Conflicts

**Problem:** Git can't automatically merge changes.

**Solution:**
1. Open conflicted files
2. Look for conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
3. Choose which version to keep (or combine)
4. Remove conflict markers
5. Stage and commit:
   ```bash
   git add filename.txt
   git commit -m "Resolve merge conflict"
   ```

### Issue: "Permission denied (publickey)"

**Problem:** SSH authentication issue.

**Solution:**
- Use HTTPS instead of SSH
- Or set up SSH keys properly

### Issue: Accidentally committed wrong files

**Solution:**
```bash
# Unstage files (keep changes)
git reset HEAD filename.txt

# Or undo last commit (keep changes)
git reset HEAD~1
```

---

# 20) Practice Exercises

### Exercise 1: Create Your First Repository

**Task:** Create a local repository, add files, and make commits.

**Steps:**
1. Create a folder: `mkdir git-practice`
2. Navigate: `cd git-practice`
3. Initialize: `git init`
4. Create a file: `echo "# My Project" > README.md`
5. Stage: `git add README.md`
6. Commit: `git commit -m "Add README"`
7. Check history: `git log --oneline`

### Exercise 2: Work with Branches

**Task:** Create a branch, make changes, and merge.

**Steps:**
1. Create branch: `git checkout -b add-feature`
2. Create file: `echo "def feature():" > feature.py`
3. Stage and commit: `git add feature.py` then `git commit -m "Add feature"`
4. Switch to main: `git checkout main`
5. Merge: `git merge add-feature`
6. Delete branch: `git branch -d add-feature`

### Exercise 3: Connect to GitHub

**Task:** Push your local repository to GitHub.

**Steps:**
1. Create repository on GitHub (don't initialize)
2. Add remote: `git remote add origin <your-repo-url>`
3. Push: `git push -u origin main`
4. Verify on GitHub website

### Exercise 4: Clone and Contribute

**Task:** Clone a repository, make changes, and push.

**Steps:**
1. Clone: `git clone <repository-url>`
2. Navigate: `cd repository-name`
3. Create branch: `git checkout -b my-changes`
4. Make changes: Edit a file
5. Commit: `git add .` then `git commit -m "My changes"`
6. Push: `git push origin my-changes`

### Exercise 5: Practice Undoing

**Task:** Practice undoing different types of changes.

**Steps:**
1. Make a change to a file (don't stage)
2. Undo: `git restore filename.txt`
3. Make change and stage: `git add filename.txt`
4. Unstage: `git restore --staged filename.txt`
5. Make commit: `git commit -m "Test commit"`
6. Undo commit (keep changes): `git reset HEAD~1`

---

# Quick Reference Card

## Daily Workflow
```bash
# 1. Check status
git status

# 2. Pull latest changes
git pull

# 3. Make changes (edit files)

# 4. Stage changes
git add .

# 5. Commit
git commit -m "Description"

# 6. Push
git push
```

## Creating New Feature
```bash
# 1. Create and switch branch
git checkout -b feature-name

# 2. Make changes and commit
git add .
git commit -m "Add feature"

# 3. Push branch
git push -u origin feature-name

# 4. Switch back to main
git checkout main

# 5. Merge feature
git merge feature-name

# 6. Push main
git push
```

## Emergency Commands
```bash
# Discard all uncommitted changes
git restore .

# Undo last commit (keep changes)
git reset HEAD~1

# View what changed
git diff

# See commit history
git log --oneline
```

---

# Additional Resources

- **Official Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com
- **Interactive Git Tutorial:** https://learngitbranching.js.org
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf

---

# Conclusion

Congratulations! You now understand the basics of Git and GitHub. Remember:

1. **Practice regularly** - The more you use Git, the more natural it becomes
2. **Start simple** - Master the basics before advanced features
3. **Don't be afraid** - Git has safety features, and you can usually undo mistakes
4. **Read error messages** - Git usually tells you what's wrong and how to fix it
5. **Use branches** - They're your friend for organizing work

**Next Steps:**
- Practice with the exercises above
- Create a personal project and use Git
- Contribute to open source projects
- Learn about pull requests and code review
- Explore advanced Git features (rebase, cherry-pick, etc.)

Happy coding! 🚀

