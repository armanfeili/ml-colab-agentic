# Quick Reference Card

## 🏃 30-Second Quickstart

```bash
# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/ml-colab-agentic.git
git branch -M main
git push -u origin main
```

Then in GitHub Settings → Check "Template repository"

---

## 🎯 Using Copilot Agents

1. Open `AGENT_MISSIONS.md`
2. Copy any mission (e.g., "Add CIFAR-10 training pipeline")
3. Paste into Copilot Chat (⌘ + i in VS Code)
4. Copilot creates PR with changes
5. Review → Merge → Run in Colab GPU

---

## 📓 Running in Colab

1. Open: [Colab Badge in README](README.md)
2. Runtime → Change runtime type → **GPU** (T4/A100)
3. Run cells 1-4
4. `outputs/metrics.csv` is created

---

## 🧪 Testing Locally

```bash
# Install
pip install -r requirements.txt pytest ruff black

# Lint
ruff check .
black --check .

# Test
pytest -q
```

---

## 📂 File Structure

| File | Purpose |
|------|---------|
| `src/utils.py` | Refactorable training utilities |
| `notebooks/01_train.ipynb` | GPU-powered notebook |
| `tests/test_smoke.py` | Quick validation |
| `.github/workflows/` | Automated CI/CD |
| `.devcontainer/` | GitHub Codespaces setup |
| `AGENT_MISSIONS.md` | Copilot Chat prompts |

---

## 🔗 Key URLs

- **Colab Notebook**: https://colab.research.google.com/github/YOUR_USERNAME/ml-colab-agentic/blob/main/notebooks/01_train.ipynb
- **Edit README**: Update `YOUR_USERNAME` in `README.md` Colab badge

---

## ✅ Checklist for New Project

- [ ] Fork or use as template
- [ ] Update README with your GitHub username
- [ ] Push to GitHub
- [ ] Try one AGENT_MISSION in Copilot
- [ ] Merge PR
- [ ] Open notebook in Colab GPU
- [ ] Run and verify

---

## 🚨 Common Issues

| Issue | Solution |
|-------|----------|
| "Module not found" in Colab | Re-run Cell 2 (pip install) |
| GPU not showing | Runtime → Change runtime type → GPU |
| Tests fail locally | Run `pip install -r requirements.txt` first |
| GitHub Actions fails | Check `.gitignore` — large files shouldn't be committed |

---

## 📞 Support

- Check `CONTRIBUTING.md` for guidelines
- Report bugs in Issues (use template)
- See `SECURITY.md` for security issues
- Read `CODE_OF_CONDUCT.md` for community norms

---

**Made with ❤️ for Colab + Copilot Agents**
