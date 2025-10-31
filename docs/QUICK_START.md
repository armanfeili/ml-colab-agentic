# Quick Start

**Run CIFAR-10 training on Colab GPU in 5 minutes.**

## 1. Open in Colab

Click the badge in [README.md](../README.md) or go to:
```
https://colab.research.google.com/github/armanfeili/ml-colab-agentic/blob/main/notebooks/01_train.ipynb
```

## 2. Set GPU

- Top right: "Code" or "Runtime"
- Runtime → Change runtime type → GPU (T4 or A100)
- Click Save

## 3. Run Cells Top-to-Bottom

**Section A: Setup**
- ✅ Cell 1: Check GPU (`!nvidia-smi`)
- ✅ Cell 2: Clone/pull repo
- ✅ Cell 3: Mount Drive (optional)
- ✅ Cell 4: Install deps
- ✅ Cell 5: Import utils

**Section B: Config**
- Edit `CFG["drive_dir"]` to your Drive path (if saving)

**Section C: Train**
- ✅ Cell 1-6: Initialize model & load data
- ✅ Cell 7: Train for 5 epochs

**Section D: Save**
- ✅ Cell 1-3: Show outputs, copy to Drive

## 4. Outputs

After training:

**Local (repo):**
- `outputs/metrics.csv` — Training metrics (epoch, loss, acc)
- `checkpoints/last.pt` — Model weights

**Google Drive** (if `save_to_drive=True`):
- `/MyDrive/ml-outputs/metrics.csv`
- `/MyDrive/ml-outputs/last.pt`

## Modify Config (Section B)

Edit this dict before training:

```python
CFG = {
    "seed": 42,              # Random seed
    "epochs": 5,             # Number of epochs
    "batch_size": 128,       # Batch size
    "lr": 1e-3,              # Learning rate
    "num_workers": 2,        # DataLoader workers
    "dataset": "CIFAR10",    # Dataset name
    "data_root": "/content/data",           # Where to download data
    "save_to_drive": True,   # Save to Drive?
    "drive_dir": "/content/drive/MyDrive/ml-outputs",  # Drive path
}
```

### Common Changes

**Use existing Drive data:**
```python
CFG["data_root"] = "/content/drive/MyDrive/data"
CFG["save_to_drive"] = False  # Don't save back
```

**Train longer:**
```python
CFG["epochs"] = 20
CFG["batch_size"] = 64  # If GPU memory is tight
```

**Disable Drive save:**
```python
CFG["save_to_drive"] = False
```

## Tips

- **First run downloads CIFAR-10** (~160 MB) — takes 1-2 min
- **Each epoch takes ~5-10 sec on GPU** (depending on T4 vs A100)
- **Total runtime: ~2 min** (setup + 5 epochs)
- **Drive save is optional** — set `save_to_drive = False` to skip

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "CUDA not available" | Check GPU runtime (Runtime → Change runtime type) |
| "CIFAR10 download fails" | Try restarting runtime (Runtime → Restart Runtime) |
| "Drive mount fails" | Cell 3 is optional; skip if not needed |
| "OOM error" | Reduce `batch_size` (e.g., 64 or 32) |
| "Permission denied to Drive" | Make sure `CFG["drive_dir"]` is accessible in your Drive |

## Next Steps

1. **Modify the code** (src/utils.py, notebook cells)
2. **Run again** in Colab to test
3. **Commit changes** to GitHub
4. **Use Copilot Chat** (⌘ + i) to propose larger changes

## Files Reference

| File | Purpose |
|------|---------|
| `notebooks/01_train.ipynb` | Main notebook (run this in Colab) |
| `src/utils.py` | Helper functions (seeding, model, train loop) |
| `requirements.txt` | Python packages to install |
| `data/` | Datasets (git-ignored) |
| `outputs/` | Metrics CSV (git-ignored) |
| `checkpoints/` | Model weights (git-ignored) |

---

**Questions?** See [../README.md](../README.md) for overview or edit notebook cells directly to experiment!
