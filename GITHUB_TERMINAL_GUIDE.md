# 🔗 Complete Guide: Connecting Your Terminal to GitHub

A comprehensive step-by-step guide for Windows users to connect their terminal to GitHub and manage their code.

---

## 📋 Table of Contents

1. [Prerequisites](#-prerequisites)
2. [Install Git](#-step-1-install-git)
3. [Configure Git](#-step-2-configure-git)
4. [Create GitHub Account](#-step-3-create-github-account)
5. [Generate Personal Access Token](#-step-4-generate-personal-access-token-https-method)
6. [Find Repository Information](#-step-5-find-repository-information)
7. [Connect Local Project to GitHub](#-step-6-connect-local-project-to-github)
8. [Daily Git Commands](#-step-7-daily-git-commands)
9. [Troubleshooting](#-troubleshooting)
10. [SSH Method (Alternative)](#-alternative-ssh-method)

---

## 📦 Prerequisites

- Windows 10 or 11
- Internet connection
- A GitHub account (or create one in Step 3)

---

## 🔧 Step 1: Install Git

### 1.1 Download Git

Go to: https://git-scm.com/download/win

### 1.2 Run the Installer

- Double-click the downloaded file
- Follow the installation prompts (default settings are fine)
- Click "Next" through all screens, then "Install"

### 1.3 Verify Installation

Open PowerShell and run:

```powershell
git --version
```

You should see something like: `git version 2.43.0`

---

## ⚙️ Step 2: Configure Git

Set your identity (use the same email as your GitHub account):

```powershell
git config --global user.name "Your Full Name"
git config --global user.email "youremail@example.com"
```

### Verify Configuration

```powershell
git config --global --list
```

### Save Credentials (So You Don't Enter Them Every Time)

```powershell
git config --global credential.helper manager
```

---

## 👤 Step 3: Create GitHub Account

1. Go to: https://github.com
2. Click **Sign Up**
3. Enter your email, create a password, choose a username
4. Verify your email address
5. Complete the setup wizard

---

## 🔑 Step 4: Generate Personal Access Token (HTTPS Method)

GitHub no longer accepts passwords. You need a Personal Access Token (PAT).

### 4.1 Go to Token Settings

1. Log in to GitHub
2. Click your **profile picture** (top right)
3. Click **Settings**
4. Scroll down and click **Developer settings** (left sidebar, bottom)
5. Click **Personal access tokens** → **Tokens (classic)**
6. Click **Generate new token** → **Generate new token (classic)**

### 4.2 Configure Your Token

- **Note:** Give it a name (e.g., "My Windows PC")
- **Expiration:** Choose 90 days, 1 year, or "No expiration"
- **Scopes:** Check the box for **repo** (this gives full repository access)

### 4.3 Generate and Save

1. Click **Generate token**
2. **⚠️ COPY THE TOKEN IMMEDIATELY** - You won't see it again!
3. Save it somewhere safe (text file, password manager, etc.)

---

## 🔍 Step 5: Find Repository Information

### 5.1 Find the Repository URL

1. Go to your repository on GitHub
2. Click the green **Code** button
3. Make sure **HTTPS** is selected
4. Copy the URL (looks like: `https://github.com/username/repo-name.git`)

### 5.2 Find Available Branches (If You Don't Know the Branch Name)

#### Method A: On GitHub Website

1. Go to your repository
2. Click the branch dropdown (usually says "main" or "master")
3. You'll see all available branches listed

#### Method B: From Terminal (After Cloning or Adding Remote)

List all remote branches:

```powershell
git branch -r
```

List all branches (local and remote):

```powershell
git branch -a
```

#### Method C: Check Remote Branches Before Cloning

```powershell
git ls-remote --heads https://github.com/username/repo-name.git
```

This shows all branches without downloading the repository.

### 5.3 Common Branch Names

- `main` - Default branch (newer repositories)
- `master` - Default branch (older repositories)
- `develop` or `dev` - Development branch
- `feature/xyz` - Feature branches
- Custom names (like `solent`, `production`, etc.)

---

## 🚀 Step 6: Connect Local Project to GitHub

### Scenario A: Starting Fresh (New Local Project)

Navigate to your project folder:

```powershell
cd "C:\path\to\your\project"
```

Initialize Git:

```powershell
git init
```

Add the remote repository:

```powershell
git remote add origin https://github.com/username/repo-name.git
```

Add all files:

```powershell
git add .
```

Create your first commit:

```powershell
git commit -m "Initial commit"
```

Set your branch name and push:

```powershell
git branch -M main
git push -u origin main
```

### Scenario B: Connecting to Existing Repository with a Specific Branch

If pushing to a specific branch (e.g., `solent`):

```powershell
git init
git remote add origin https://github.com/username/repo-name.git
git add .
git commit -m "Initial commit"
git branch -M solent
git pull origin solent --allow-unrelated-histories
git push -u origin solent
```

### Scenario C: Clone an Existing Repository

Download an existing repository:

```powershell
git clone https://github.com/username/repo-name.git
```

Clone a specific branch:

```powershell
git clone -b branch-name https://github.com/username/repo-name.git
```

### When Prompted for Credentials

- **Username:** Your GitHub username
- **Password:** Your **Personal Access Token** (NOT your GitHub password!)

---

## 📝 Step 7: Daily Git Commands

### Check Status

See what files have changed:

```powershell
git status
```

### Save Your Changes

```powershell
git add .
git commit -m "Describe what you changed"
git push
```

### Get Latest Changes from GitHub

```powershell
git pull
```

### View Commit History

```powershell
git log --oneline
```

### Switch Branches

```powershell
git checkout branch-name
```

Or create and switch to a new branch:

```powershell
git checkout -b new-branch-name
```

### See All Branches

```powershell
git branch -a
```

---

## 🔧 Troubleshooting

### Error: "remote origin already exists"

Remove the existing remote and add again:

```powershell
git remote remove origin
git remote add origin https://github.com/username/repo-name.git
```

### Error: "failed to push - rejected (non-fast-forward)"

Your local branch is behind the remote. Pull first:

```powershell
git pull origin branch-name --allow-unrelated-histories
git push
```

Or force push (⚠️ overwrites remote - use carefully!):

```powershell
git push --force
```

### Error: "Authentication failed"

1. Make sure you're using your Personal Access Token, not your password
2. Generate a new token if the old one expired
3. Clear saved credentials:

```powershell
git credential-manager erase
```

### Stuck in Vim Editor

When Git opens a text editor for merge messages:

1. Press **Esc**
2. Type `:wq`
3. Press **Enter**

### Check Current Remote URL

```powershell
git remote -v
```

### Change Remote URL

```powershell
git remote set-url origin https://github.com/username/new-repo.git
```

---

## 🔐 Alternative: SSH Method

SSH is more secure and doesn't require entering credentials each time.

### Generate SSH Key

```powershell
ssh-keygen -t ed25519 -C "youremail@example.com"
```

Press Enter to accept defaults. Set a passphrase if desired.

### Start SSH Agent

```powershell
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
```

### Add Key to SSH Agent

```powershell
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

### Copy Public Key

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard
```

### Add Key to GitHub

1. Go to GitHub → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Paste your key and save

### Test SSH Connection

```powershell
ssh -T git@github.com
```

### Use SSH URL Instead of HTTPS

```powershell
git remote set-url origin git@github.com:username/repo-name.git
```

---

## 📚 Quick Reference Card

| Task | Command |
|------|---------|
| Initialize repository | `git init` |
| Check status | `git status` |
| Add all files | `git add .` |
| Commit changes | `git commit -m "message"` |
| Push to GitHub | `git push` |
| Pull from GitHub | `git pull` |
| Clone repository | `git clone <url>` |
| See branches | `git branch -a` |
| Switch branch | `git checkout <branch>` |
| Create new branch | `git checkout -b <branch>` |
| View commit history | `git log --oneline` |
| Check remote URL | `git remote -v` |

---

## ✅ Success Checklist

- [ ] Git installed and verified
- [ ] Git configured with name and email
- [ ] GitHub account created
- [ ] Personal Access Token generated and saved
- [ ] Repository URL copied
- [ ] Branch name identified
- [ ] Local project connected to GitHub
- [ ] First push successful

---

## 🎉 You're All Set!

Your terminal is now connected to GitHub. Happy coding!

---

*Guide created: December 2024*
*For: Solent University - Problem Solving Through Programming QH0444*

