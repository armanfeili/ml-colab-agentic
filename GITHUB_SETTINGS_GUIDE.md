# GitHub Repository Settings Guide

## Once You Push to GitHub

These settings will help you maintain quality and automation.

### 1. Enable "Template Repository"

**Location:** Settings → General → Repository template

- Check: ✓ "Template repository"
- This allows users to click "Use this template" to create new projects from yours

### 2. Add Repository Topics

**Location:** Repository home → About (⚙️ gear icon) → Edit

Add these topics:
- `template`
- `colab`
- `gpu`
- `ml`
- `copilot`
- `agentic`
- `jupyter`
- `pytorch`

This makes your repo discoverable and categorized.

### 3. Branch Protection (Recommended)

**Location:** Settings → Branches → Add rule

**Branch name pattern:** `main`

**Protect this branch:**
- ✓ Require a pull request before merging
  - ✓ Require approvals: 1
  - ✓ Dismiss stale pull request approvals when new commits are pushed
- ✓ Require status checks to pass before merging
  - Search for: `run-notebook` (select the smoke test workflow)
  - ✓ Require branches to be up to date before merging
- ✓ Restrict who can push to matching branches (optional)

**Why:** Ensures every change goes through code review and CI testing.

### 4. Actions Permissions

**Location:** Settings → Actions → General

- Select: "Allow all actions and reusable workflows"
- Save

**Why:** Enables GitHub Actions to run your smoke test on PRs.

### 5. Environment Secrets (Optional - Future Use)

**Location:** Settings → Environments or Secrets

If you later add integrations (wandb, hugging face, etc.), add secrets here.

### 6. Configure Dependabot (Optional)

**Location:** Settings → Code security and analysis

- Enable: "Dependabot alerts"
- Enable: "Dependabot security updates"

**Why:** Automatically alerts you to security vulnerabilities in dependencies.

---

## Quick Checklist

After pushing to GitHub, run through:

- [ ] Repository is public (check Settings → General)
- [ ] Template repository is enabled
- [ ] Colab badge in README opens notebook correctly
- [ ] Added repository topics
- [ ] Main branch protection enabled (at least require PR)
- [ ] GitHub Actions are enabled
- [ ] Ran CI smoke test on a PR (to verify workflow)
