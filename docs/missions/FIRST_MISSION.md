# 🤖 First Copilot Agent Mission - Quick Start

## Mission: Add CIFAR-10 Training Pipeline

### How to Use This

1. **Open VS Code** with this repo
2. **Open Copilot Chat** (⌘ + i or GitHub.copilot-chat extension)
3. **Copy the mission below** (or open AGENT_MISSIONS.md and copy Mission 1)
4. **Paste into Copilot Chat**
5. **Press Enter** → Let Copilot analyze and propose changes
6. **Review the PR** → Merge when satisfied

---

## Copy & Paste This Mission:

```
I want to add a CIFAR-10 training pipeline to this ML Colab Agentic template repository.

Here's what I need:
1. Inspect `notebooks/01_train.ipynb` and `src/utils.py` to understand the current structure
2. Implement a clean CIFAR-10 pipeline with:
   - Dataset loading & transforms using torchvision
   - Simple CNN model (ResNet-18 or similar)
   - Train/validation loop with loss and accuracy tracking
   - Log metrics to `outputs/metrics.csv` (columns: epoch, train_loss, val_loss, train_acc, val_acc)
3. Keep dependencies minimal (only torch, torchvision, numpy, pandas)
4. Add unit tests in `tests/` directory for new utility functions
5. Add a new notebook cell that demonstrates the full pipeline end-to-end
6. Update `README.md` with a "CIFAR-10 Benchmark" section showing expected performance
7. Open a PR with a clear summary of changes and why

Focus on clean, readable, well-documented code that's easy for future developers to modify for other datasets.
```

---

## What Happens Next

1. **Copilot analyzes** your repo structure
2. **Proposes changes** to:
   - `src/utils.py` (add new utility functions)
   - `notebooks/01_train.ipynb` (add training cells)
   - `tests/` (add new tests)
   - `README.md` (add documentation)
   - `requirements.txt` (add new dependencies)
3. **Creates a PR** with all changes
4. **You review** the PR
5. **Merge** → GitHub Actions runs smoke test
6. **Test in Colab** → Open notebook, set GPU runtime, run cells

---

## Tips for Success

✅ **Be specific** about what you want (the more detail, the better)
✅ **Reference files** by path (e.g., `src/utils.py`, `notebooks/`)
✅ **Mention constraints** (dependencies, style, etc.)
✅ **Ask for tests** (Copilot will add them)
✅ **Request docs** (Copilot will update README)

---

## After the First Mission

Try these in order of difficulty:

1. ✅ **Mission 1** (this one) - CIFAR-10 pipeline
2. 📈 **Mission 2** - A100 GPU optimization (mixed precision, larger batches)
3. 🔄 **Mission 3** - Data augmentation & regularization
4. 🤝 **Mission 4** - Distributed training (DDP)
5. 💾 **Mission 5** - Model checkpointing & resumption
6. 📊 **Mission 6** - Experiment tracking (wandb)
7. 🎯 **Mission 7** - LoRA fine-tuning
8. 📈 **Mission 8** - Evaluation & test metrics

See `AGENT_MISSIONS.md` for details on each.

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Copilot doesn't understand your repo | Add more context (mention specific files) |
| PR has import errors | Add the new deps to `requirements.txt` |
| Tests fail locally | NumPy issue on macOS? It works fine in Colab |
| Notebook doesn't run in Colab | Make sure you installed deps in Cell 2 |

---

**Ready? Open Copilot Chat and paste the mission! 🚀**
