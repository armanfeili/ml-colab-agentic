# ML Colab Training Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/armanfeili/ml-colab-agentic/blob/main/notebooks/01_train.ipynb)

A simple starting point for machine learning projects that run on Google Colab's free GPUs. The code lives on GitHub, but training happens in Colab.

## Cloud-only storage (Google Drive)

This project trains entirely on Colab GPUs and stores datasets, runs, checkpoints, metrics, plots, and artifacts in Google Drive:

- **Data:**     `/content/drive/MyDrive/ml-colab-agentic/data/{raw,processed}`
- **Runs:**     `/content/drive/MyDrive/ml-colab-agentic/runs/<run_id>/`
- **Latest:**   `/content/drive/MyDrive/ml-colab-agentic/latest/run`

Code stays in GitHub. Edit locally with Copilot → push → open notebook in Colab.

## How to Use This

**1. Start training right now:**

- Click the badge above
- In Colab: Runtime → Change runtime type → T4 GPU
- Run all cells (Runtime → Run all)
- Wait ~2 minutes
- Done! You'll have a trained model and metrics on your Drive

**2. Work with your own data:**

The example uses CIFAR-10, but you can swap it out:

```python
# In the notebook, Section A (run setup cell), change the CFG:
CFG = {
    "dataset": "YOUR_DATASET",           # Change this
    "data_root": f"{DATA_DIR}/raw",      # Points to Drive
    "epochs": 10,                        # Train longer
    "batch_size": 64,                    # Adjust for GPU memory
    # ... other settings
}
```

Then in `src/utils.py`, add a function like:

```python
def prepare_dataloaders_YOUR_DATASET(root, batch_size, num_workers):
    # Load your dataset here
    # Return (train_loader, test_loader)
```

**3. Access your results:**

Everything is saved to Google Drive automatically:

- **Metrics:** `runs/<run_id>/metrics.csv` - tracks loss and accuracy each epoch
- **Checkpoints:** `runs/<run_id>/checkpoints/` - epoch_###.pt and best.pt
- **Plots:** `runs/<run_id>/plots/{train,val,test,calib}/` - for your visualizations
- **Artifacts:** `runs/<run_id>/artifacts/{train,val,test,calib}/` - predictions, confusion matrices, etc.

Access from any device: Google Drive → MyDrive → ml-colab-agentic → runs → `<run_id>`

## What's in Here

```
notebooks/01_train.ipynb    Your main workspace - edit this in Colab
src/utils.py                Helper functions (dataloaders, model, training loop)
requirements.txt            PyTorch and a few essentials
data/                       Downloads go here (gitignored, not committed)
outputs/                    Your metrics CSV (gitignored)
checkpoints/                Your model files (gitignored)
```

## Working with Your Own Notebook

Want to start from scratch? Here's the pattern:

**Section A - Setup:**

```python
# Check you have a GPU
!nvidia-smi

# Clone this repo (or your fork)
!git clone https://github.com/YOUR_USERNAME/ml-colab-agentic.git
%cd ml-colab-agentic

# Mount Drive if you want to save stuff
from google.colab import drive
drive.mount('/content/drive')

# Install dependencies
!pip install -q -r requirements.txt

# Import your utilities
from src.utils import *
```

**Section B - Configuration:**

```python
# Put all your settings in one place
CFG = {
    "seed": 42,
    "epochs": 5,
    "batch_size": 128,
    "save_to_drive": True,
    "drive_dir": "/content/drive/MyDrive/my-project"
}
```

**Section C - Train:**

```python
# Use the functions from src/utils.py
set_seed(CFG["seed"])
device = get_device()
train_dl, test_dl = prepare_dataloaders_YOURDATA(...)

model = YourModel().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=CFG["lr"])

for epoch in range(CFG["epochs"]):
    train_loss, train_acc = train_one_epoch(model, train_dl, optimizer, device)
    test_loss, test_acc = evaluate(model, test_dl, device)
    # Log metrics, save checkpoints...
```

**Section D - Save:**

```python
# Save locally
save_checkpoint(model, "checkpoints/final.pt")

# Copy to Drive
if CFG["save_to_drive"]:
    !cp -r outputs/ checkpoints/ $CFG["drive_dir"]
```

## Storing Your Outputs

You have three options:

### 1. Timestamped runs (built-in)

Every time you run the notebook, a new timestamped folder is created:

```
runs/<run_id>/
  cfg.yaml                              # frozen config for this run
  metrics.csv                           # long-form metrics (split, epoch, metric, value)
  logs.txt                              # (optional) training logs
  checkpoints/                          # epoch_###.pt, best.pt
  artifacts/{train,val,test,calib}/     # saved predictions, embeddings, etc.
  plots/{train,val,test,calib}/         # training curves, confusion matrices
  cache/                                # temporary data for this run
```

The root-level `outputs/` and `checkpoints/` folders are **symlinks** (or copies) pointing to the **latest run**, so you always know where to find the most recent results.

### 2. Google Drive (recommended for persistence)

Mount Drive and the notebook automatically copies files there:

```python
# In the notebook's run-management cell
SAVE_TO_DRIVE = True
DRIVE_DIR = "/content/drive/MyDrive/ml-colab-agentic"
```

After training, your run folder is copied to Drive and persists forever.

### 3. Download manually

After training, click the folder icon in Colab's sidebar, navigate to `runs/<run_id>/`, right-click files → Download.

## Tips

- **GPU runtime:** T4 is free and plenty fast for small models
- **Runtime limits:** Free tier disconnects after ~12 hours. Save checkpoints often.
- **Data in Drive:** If your dataset is on Drive, dataloading is slower. Download to `/content/` first.
- **Git workflow:** Edit code locally with VS Code + Copilot, push to GitHub, pull in Colab

## Local Development (Optional)

You don't need to run anything locally - Colab does it all. But if you want to:

```bash
git clone https://github.com/armanfeili/ml-colab-agentic.git
cd ml-colab-agentic
pip install -r requirements.txt
pytest tests/  # Quick smoke tests
```

Edit `src/utils.py` with your IDE, commit changes, push to GitHub. Next time you run the Colab notebook, it pulls your updates.

## License

MIT - do whatever you want with this.
