# ML Colab Training Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/armanfeili/ml-colab-agentic/blob/main/notebooks/01_train.ipynb)

A simple starting point for machine learning projects that run on Google Colab's free GPUs. The code lives on GitHub, but training happens in Colab.

## How to Use This

**1. Start training right now:**

- Click the badge above
- In Colab: Runtime → Change runtime type → T4 GPU
- Run all cells (Runtime → Run all)
- Wait ~2 minutes
- Done! You'll have a trained model and metrics

**2. Work with your own data:**

The example uses CIFAR-10, but you can swap it out:

```python
# In the notebook, Section B, change the CFG:
CFG = {
    "dataset": "YOUR_DATASET",           # Change this
    "data_root": "/content/data",        # Or point to Drive
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

**3. Save your work:**

Everything important gets saved automatically:

- **Metrics:** `outputs/metrics.csv` - tracks loss and accuracy each epoch
- **Model:** `checkpoints/last.pt` - the trained model weights
- **To Google Drive:** Set `save_to_drive: True` in CFG to copy everything there

The notebook itself? Save it back to GitHub:

- File → Save a copy in GitHub
- Or download it: File → Download → Download .ipynb

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

**1. Colab's temporary storage (default)**

Files save to `/content/` but disappear when runtime disconnects. Fine for quick experiments.

**2. Google Drive (recommended)**

Mount Drive and copy files there. They persist forever:

```python
# In Section A
from google.colab import drive
drive.mount('/content/drive')

# In Section D
!mkdir -p /content/drive/MyDrive/my-ml-project
!cp outputs/metrics.csv /content/drive/MyDrive/my-ml-project/
!cp checkpoints/best.pt /content/drive/MyDrive/my-ml-project/
```

**3. Download manually**

After training, click the folder icon in Colab's sidebar, right-click files → Download.

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
