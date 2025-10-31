# ML Colab Agentic

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/armanfeili/ml-colab-agentic/blob/main/notebooks/01_train.ipynb)

**A minimal, Colab-first training template.** Clone it locally, develop with Copilot, train on GPU.

## Quick Start (4 steps)

1. **Click the badge** above → Opens this notebook in Colab
2. **Set GPU** → Runtime → Change runtime type → GPU (T4 or A100)
3. **Run cells** → Section A (Setup) → Section C (Train) → outputs/metrics.csv
4. **Optional** → Save notebook back to GitHub (File → Save a copy in GitHub)

## What It Does

- Clones this repo into `/content/ml-colab-agentic`
- Mounts your Google Drive (optional)
- Downloads CIFAR-10 dataset
- Trains a simple CNN for 5 epochs on GPU
- Saves metrics and checkpoint to:
  - `outputs/metrics.csv` (local + Drive)
  - `checkpoints/last.pt` (local + Drive)

## Files

```
notebooks/
  └── 01_train.ipynb       ← Edit & run in Colab (GPU)

src/
  └── utils.py             ← Seeding, dataloaders, SimpleNet, train/eval

requirements.txt           ← Minimal deps (torch, pandas, etc)
data/                      ← Datasets (not committed; .gitignored)
outputs/                   ← Metrics CSV (not committed)
checkpoints/               ← Model weights (not committed)
```

## Config (Section B)

Edit `CFG` dict in the notebook:

```python
CFG = {
    "seed": 42,
    "epochs": 5,
    "batch_size": 128,
    "lr": 1e-3,
    "num_workers": 2,
    "dataset": "CIFAR10",
    "data_root": "/content/data",
    "save_to_drive": True,
    "drive_dir": "/content/drive/MyDrive/ml-outputs"  # ← Change this
}
```

## Datasets

In Colab, datasets are downloaded to `/content/data` (not committed).

To use Google Drive:

- Mount Drive (Section A, cell 3)
- Update `CFG["data_root"] = "/content/drive/MyDrive/data"`

## Development

**Local setup** (optional; tests pass in Colab):

```bash
git clone <repo>
cd ml-colab-agentic
pip install -r requirements.txt
pytest tests/  # Smoke test
```

**With Copilot Chat** (⌘ + i in VS Code):

- Propose changes → Copilot creates PR
- Review & merge → Run notebook in Colab

## v0.2.0 Release Notes

- ✅ Colab-first design (everything runs in `/content/`)
- ✅ Minimal dependencies (torch, pandas, matplotlib, tqdm)
- ✅ 4-section notebook (Setup, Config, Train, Save)
- ✅ Auto-save to Google Drive (optional)
- ✅ Simple utils: seeding, dataloaders, SimpleNet, metrics CSV

## License

MIT — see [LICENSE](LICENSE)
