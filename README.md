# ML Colab Agentic Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/armanfeili/ml-colab-agentic/blob/main/notebooks/01_train.ipynb)

A minimal and reproducible template for training machine learning models in Google Colab using free GPUs. Code is versioned on GitHub. All data, models, and results are stored in Google Drive.

---

## Features

* Train directly in Colab using GPU runtime
* Store datasets, checkpoints, metrics, and plots in Google Drive
* Clean separation between code (GitHub) and storage (Drive)
* Compatible with GitHub Copilot and local development
* Simple structure for reproducible experiments

---

## Google Drive Folder Structure

```
MyDrive/ml-colab-agentic/
├── data/
│   ├── raw/            # Unprocessed source files
│   └── processed/      # Ready-to-use datasets
├── runs/
│   └── <run_id>/       # Example: 2025-10-31_17-20_cifar10
│       ├── cfg.yaml
│       ├── metrics.csv
│       ├── checkpoints/
│       ├── artifacts/
│       ├── plots/
│       └── cache/
├── latest/
│   └── run             # Optional: symlink to most recent run
```

---

## Quick Start

1. Click the badge above
2. In Colab: go to Runtime > Change runtime type > select GPU (T4)
3. Run all cells
4. Training starts; results are saved in your Google Drive

---

## Project Layout

| Path                       | Description                                       |
| -------------------------- | ------------------------------------------------- |
| `notebooks/01_train.ipynb` | Main notebook for training (run in Colab)         |
| `src/utils.py`             | Helper functions for model, dataloaders, training |
| `data/`                    | Local or Drive-synced data (not committed)        |
| `runs/`                    | Output directory for each experiment              |
| `requirements.txt`         | Python dependencies                               |
| `checkpoints/`, `outputs/` | Optional: shortcuts to latest run results         |

---

## Using a Custom Dataset

1. Edit the config in the notebook:

```python
CFG = {
    "dataset": "your_dataset",
    "data_root": f"{DATA_DIR}/raw",
    "epochs": 10,
    "batch_size": 64,
}
```

2. Add your dataset loader in `src/utils.py`:

```python
def prepare_dataloaders_your_dataset(root, batch_size, num_workers):
    # Load and return train and test loaders
```

---

## Outputs per Run

Each training run creates a dedicated folder in Drive:

```
runs/<run_id>/
├── cfg.yaml              # Frozen config
├── metrics.csv           # Epoch-wise results
├── checkpoints/          # All saved model weights
├── artifacts/            # Confusion matrices, outputs, etc.
├── plots/                # Learning curves, calibration plots
├── cache/                # Temporary or precomputed data
```

`outputs/` and `checkpoints/` may point to the latest run.

---

## Tips

* Free Colab GPUs (T4) are sufficient for many models
* Mount Drive to persist data across sessions
* Use VS Code and GitHub Copilot locally for development
* Push code changes to GitHub, then pull from Colab

---

## Optional: Local Development

```bash
git clone https://github.com/armanfeili/ml-colab-agentic.git
cd ml-colab-agentic
pip install -r requirements.txt
pytest tests/
```

Modify `src/utils.py`, commit and push. The next Colab session will reflect your changes.

---

## License

This project is licensed under the MIT License.
