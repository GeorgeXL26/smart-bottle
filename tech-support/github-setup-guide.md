# GitHub Setup & Workflow Guide

A beginner-friendly guide for junior developers to get started with GitHub.

---

## 1. Setting Up a GitHub Account

### Step 1: Create an Account
1. Go to https://github.com
2. Click **Sign up**
3. Enter your email, create a password, and choose a username
4. Verify your email address

### Step 2: Install Homebrew (macOS only)

Homebrew is a package manager that makes installing tools like Git easy.

**Check if you already have Homebrew:**
```bash
brew --version
```

**Install Homebrew:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen prompts. You may be asked to install Xcode Command Line Tools — confirm when prompted.

**After installation, follow the "Next Steps" printed in the terminal** to add Homebrew to your PATH. It's usually something like:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

If you're on an Intel Mac, the path may be `/usr/local/bin/brew` instead.

**Video guide:** [How to Install Homebrew on Mac](https://www.youtube.com/watch?v=a9u2yZvsqHA)

### Step 3: Install Git on Your Computer

**macOS:**
```bash
brew install git
```

**Windows:**
Download from https://git-scm.com/download/win

**Linux (Ubuntu/Debian):**
```bash
sudo apt install git
```

### Step 4: Configure Git
Open your terminal and set your name and email (use the same email as your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 5: Authenticate with GitHub (Token)

1. Go to https://github.com/settings/tokens
2. Click **Generate new token** > **Fine-grained token**
3. Set the expiration and select `Contents` read/write permission
4. Click **Generate token** and **copy the token immediately** (you won't see it again)
5. Use the token for authentication:

```bash
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"
```

To make it permanent, add it to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
echo 'export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"' >> ~/.zshrc
source ~/.zshrc
```

---

## 2. Cloning a Repository

To download a repo to your computer:

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

---

## 3. Creating a Branch

Branches let you work on features without affecting the main codebase.

### Check your current branch:
```bash
git branch
```

### Create and switch to a new branch:
```bash
git checkout -b feature/your-feature-name
```

- `feature/your-feature-name` is the branch name. Use descriptive names like `feature/add-login` or `fix/typo-in-readme`
- The `-b` flag creates the branch AND switches to it

### Switch between branches:
```bash
git checkout main           # switch to main
git checkout feature/xxx    # switch to your feature branch
```

---

## 4. Making Changes & Committing

### Step 1: Check what's changed:
```bash
git status
```

### Step 2: Stage your changes:
```bash
git add filename.md           # stage a specific file
git add .                     # stage all changes (use carefully)
```

### Step 3: Commit your changes:
```bash
git commit -m "Your commit message"
```

**Good commit message rules:**
- Use present tense: "Add login button" not "Added login button"
- Be specific: "Fix typo in README" not "Fix stuff"
- Keep it under 50 characters if possible

---

## 5. Pushing to GitHub

Send your committed changes to the remote repository:

```bash
git push origin your-branch-name
```

**First time pushing a new branch?** Set the upstream:
```bash
git push -u origin your-branch-name
```

The `-u` flag links your local branch to the remote one so future pushes are just `git push`.

---

## 6. Creating a Pull Request (PR)

A PR is how you ask to merge your changes into the main branch.

### Via GitHub Website:
1. Push your branch (see section 5)
2. Go to your repo on GitHub — you'll see a yellow banner suggesting your branch
3. Click **Compare & pull request**
4. Add a title and description
5. Click **Create pull request**

### Via GitHub CLI (`gh`):
```bash
gh pr create --title "Your PR title" --body "Description of changes"
```

### PR best practices:
- Write a clear title and description explaining **what** and **why**
- Keep PRs focused on one thing (don't mix unrelated changes)
- Review your own diff before requesting review
- Tag reviewers if needed

---

## 7. Rebasing

Rebasing keeps your branch up to date with the latest changes from `main`.

### Why rebase?
- Avoids merge conflicts later
- Keeps a clean, linear git history
- Ensures your branch works with the latest code

### How to rebase:

```bash
# 1. Switch to your feature branch
git checkout your-feature-branch

# 2. Fetch the latest changes from main
git fetch origin main

# 3. Rebase your branch onto main
git rebase origin/main
```

### If you get conflicts during rebase:
1. Git will pause and tell you which files have conflicts
2. Open those files and look for `<<<<<<<`, `=======`, `>>>>>>>` markers
3. Edit the files to keep the correct code and remove the markers
4. Save the files, then:

```bash
git add file-with-conflict.md
git rebase --continue
```

5. Write a commit message for the merge (or just save and exit)
6. If you get stuck at any point, abort with:

```bash
git rebase --abort
```

### Push after rebasing:
Since rebase rewrites history, use force push:

```bash
git push origin your-feature-branch --force-with-lease
```

> `--force-with-lease` is safer than `--force` — it checks that no one else pushed to your branch first.

---

## 8. Quick Reference

| Command | What it does |
|---------|-------------|
| `git status` | Check current state |
| `git branch` | List branches |
| `git checkout -b name` | Create & switch to new branch |
| `git add file` | Stage a file |
| `git commit -m "msg"` | Commit staged changes |
| `git push -u origin branch` | Push and set upstream |
| `git fetch origin main` | Get latest main changes |
| `git rebase origin/main` | Rebase current branch onto main |
| `git push --force-with-lease` | Push after rebasing |
| `gh pr create` | Create a pull request |

---

## 9. Windows-Specific Guide

If you're on Windows, here's everything you need to get set up properly.

### Terminal Options

You have three choices for running Git commands on Windows:

| Option | Best for | How to get it |
|--------|----------|--------------|
| **Git Bash** | Beginners, simplest setup | Comes with Git for Windows |
| **PowerShell** | Windows power users | Built into Windows 10/11 |
| **WSL (Ubuntu)** | Full Linux experience | Install via `wsl --install` in PowerShell |

**Recommended for beginners:** Git Bash — it works like macOS/Linux terminals and all commands in this guide work as-is.

### Installing Git on Windows

1. Download from https://git-scm.com/download/win
2. Run the installer
3. **Important settings during installation:**
   - **Select Components:** Keep defaults, make sure "Git Bash Here" is checked
   - **Default editor:** Choose VS Code (if installed) or Nano
   - **Adjust PATH:** Select "Git from the command line and also from 3rd-party software" (recommended)
   - **Line ending conversions:** Select "Checkout as-is, commit Unix-style line endings"
4. Complete the installation

After install, right-click in any folder and select **Git Bash Here** to open Git Bash.

### Setting Up Git Bash Profile (Token Persistence)

Unlike macOS/Linux where you edit `~/.zshrc`, on Git Bash you edit `~/.bashrc`:

```bash
echo 'export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc
```

### Using PowerShell (Alternative)

If you prefer PowerShell:

```powershell
# Set token for current session
$env:GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxx"

# Make it permanent (add to your PowerShell profile)
notepad $PROFILE
# Add this line to the file that opens:
# $env:GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxx"
```

### Windows Path Notes

- Windows uses backslashes (`\`) but Git Bash understands forward slashes (`/`) too
- Your Windows `C:` drive is at `/c/` in Git Bash
- Example: `cd /c/Users/YourName/projects`

### Installing WSL (Optional, for advanced users)

WSL lets you run a full Linux environment on Windows:

```powershell
# Run in PowerShell as Administrator
wsl --install
```

After install, you'll have Ubuntu with a Linux terminal — all macOS/Linux commands in this guide work identically.

### GUI Tool: GitHub Desktop

For junior developers who prefer a visual interface:

1. Download from https://desktop.github.com
2. Install and sign in with your GitHub account
3. Clone repos, create branches, and make PRs with buttons instead of commands

### Windows-Specific Troubleshooting

| Problem | Solution |
|---------|----------|
| `git` not recognized | Re-run Git installer and select "Add to PATH" |
| Line ending warnings | Run `git config --global core.autocrlf true` |
| Permission denied (public key) | You're using SSH but set up a token — use HTTPS URLs instead |
| Credential popup every time | Set up token as shown above, or run `git config --global credential.helper wincred` |

### Common Windows Commissions Reference

```powershell
# Check Git version
git --version

# Check where Git is installed
where git

# Open current folder in File Explorer
explorer .

# Clear the terminal
cls
```

---

## Common Pitfalls to Avoid

- **Committing on `main`** — always create a feature branch first
- **Forgetting to pull before rebasing** — always `git fetch` first
- **Force pushing shared branches** — only force push your own feature branches
- **Vague commit messages** — write messages that explain the *why*, not just the *what*
