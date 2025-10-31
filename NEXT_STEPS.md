# Next Steps Guide

## 1. Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named: **ml-colab-agentic**
3. **Important:** Do NOT initialize with README, license, or .gitignore (to avoid conflicts)
4. Leave it completely empty

## 2. Push Your Code

Replace `<YOUR_USERNAME>` with your GitHub username and run:

```bash
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/ml-colab-agentic.git
git push -u origin main
```

## 3. Update Placeholders

After pushing, you need to update `<YOUR_USERNAME>` in two places:

### A. README.md
Find and replace `<YOUR_USERNAME>` with your actual GitHub username in the Colab badge URL.

### B. notebooks/01_train.ipynb
In cell #2 (Install Requirements), replace `<YOUR_USERNAME>` with your actual GitHub username.

Then commit and push:
```bash
git add README.md notebooks/01_train.ipynb
git commit -m "docs: update username placeholders"
git push
```

## 4. Verify Colab Integration

1. Open your README on GitHub
2. Click the "Open in Colab" badge
3. In Colab:
   - Runtime → Change runtime type → **GPU** (T4/A100)
   - Run all cells
   - Verify `!nvidia-smi` shows GPU
   - Training should complete and save metrics

## 5. Create Agent Mission Issue (Optional)

Create a new issue on GitHub with this content:

**Title:** Agent Mission: Upgrade training to CIFAR-10 + AMP + val split

**Body:**
```
Mission:
- Replace FakeData with CIFAR-10 (download in-notebook).
- Add validation split + accuracy metrics.
- Add AMP (torch.cuda.amp) for faster GPU training.
- Add simple plots of loss/acc over epochs and save to outputs/.
- Pin package versions in requirements.txt.
- Open a PR with a summary of changes.

Constraints:
- Keep dependencies minimal.
- Keep notebook runnable in Colab GPU (Pro/Pro+).
- Leave clear comments where user secrets or Drive mounting would be added.
```

Then ask Copilot Chat/Agent to execute this mission and open a PR.

## 6. Your Repository is Ready! 🎉

You now have:
- ✅ Complete folder structure
- ✅ Working Colab notebook with GPU support
- ✅ Dev container configuration
- ✅ CI/CD workflow for notebook testing
- ✅ Git initialized with first commit
- ✅ Ready to push to GitHub

Happy coding with Copilot + Colab! 🚀
