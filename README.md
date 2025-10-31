# ML Colab Agentic

Repo template for running heavy GPU workloads in **Google Colab (Pro/Pro+)** while using **GitHub Copilot (Chat/Agents)** to plan/refactor code and open PRs.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/<YOUR_USERNAME>/ml-colab-agentic/blob/main/notebooks/01_train.ipynb)

## Workflow
1. Use Copilot Chat/Agents in VS Code or Codespaces to edit code & notebooks (open PRs).
2. Open the notebook in Colab → set GPU runtime → run experiments.
3. Save outputs to `/content/outputs` or Google Drive; sync code changes back via PRs.

## Quick start (Colab)
- Runtime → Change runtime type → GPU (T4/A100 on Pro/Pro+)
- Run the first cells:
  - `!nvidia-smi`
  - pip install requirements from this repo URL
- Train the toy model; inspect metrics in `outputs/`

## Structure
- `notebooks/` – Colab-ready notebooks
- `src/` – Python modules used by notebooks
- `data/`, `outputs/` – local-only (gitignored)
