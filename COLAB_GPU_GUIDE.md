# Colab GPU Smoke Test Guide

## Before You Begin

1. **Create GitHub repo** with empty initialization (no README, license, .gitignore)
2. **Push this local repo** to GitHub using the commands in `GITHUB_PUSH_INSTRUCTIONS.md`
3. **Repository Settings** → Enable "Template repository"

## Running on Colab GPU

### Step 1: Open the Notebook

Click the **"Open in Colab"** badge in the README.md:
- This will open: `https://colab.research.google.com/github/armanfeili/ml-colab-agentic/blob/main/notebooks/01_train.ipynb`

### Step 2: Set GPU Runtime

1. Click **Runtime** menu (top right)
2. Select **Change runtime type**
3. Choose **T4 GPU** (or A100 if available)
4. Click **Save**

Colab will automatically restart your session.

### Step 3: Run Cells

Execute cells in order:

**Cell 1: GPU Check**
```python
!nvidia-smi
```
You should see GPU details (T4 or A100).

**Cell 2: Install Dependencies**
```python
!pip -q install -r https://raw.githubusercontent.com/armanfeili/ml-colab-agentic/main/requirements.txt
```
This installs torch, numpy, pandas, etc. from repo requirements.

**Cell 3: PyTorch Demo**
```python
import torch
from src.utils import set_seed, to_device

set_seed(0)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {device}")

# ... toy training loop ...
```
You should see:
- Device: cuda
- 5 epochs of loss decreasing
- ✅ Toy training loop completed!

**Cell 4: Save Metrics**
```python
import pathlib

pathlib.Path("outputs").mkdir(exist_ok=True)

with open("outputs/metrics.csv", "w") as f:
    f.write("epoch,loss\n")
    for i in range(5):
        f.write(f"{i},0.{i}\n")

print("✅ Wrote outputs/metrics.csv")
!ls -la outputs/
```
You should see `outputs/metrics.csv` listed.

### Step 4: (Optional) Save to GitHub

If you made changes in Colab and want to save:

1. Click **File** → **Save a copy in GitHub**
2. Select your repo: `armanfeili/ml-colab-agentic`
3. Leave branch as `main` (or create a new branch)
4. Colab will create a commit automatically

### Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'torch'` | Re-run Cell 2 (pip install) |
| GPU not showing in `!nvidia-smi` | Runtime → Change runtime type → GPU → Save |
| `FileNotFoundError: outputs` | Run Cell 4 to create the outputs folder |
| Import errors from src.utils | Make sure Cell 2 completes successfully |

## Next Steps After Smoke Test

✅ **Verified in Colab GPU** → You're ready to use the template!

1. Fork this repo for your next ML project
2. Try a Copilot Agent mission (see `AGENT_MISSIONS.md`)
3. Develop locally → Create PR → Smoke test runs → Merge → Run in Colab GPU
