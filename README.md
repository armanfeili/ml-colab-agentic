# ML Colab Agentic (Template)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/armanfeili/ml-colab-agentic/blob/main/notebooks/01_train.ipynb)

A reusable base template for projects that:
- Develop with **GitHub Copilot Chat/Agents** (planning, refactors, PRs)
- Execute heavy code on **Google Colab GPUs** (Pro/Pro+)
- Version everything in **GitHub**

## Quick start
1. Fork this repo and rename it for your new project.
2. Open `notebooks/01_train.ipynb` in Colab (GPU runtime).
3. Use Copilot Chat/Agents in VS Code/Codespaces to plan edits; merge PRs.
4. Rerun the notebook in Colab to leverage GPUs.

## Repo layout

```
ml-colab-agentic/
├─ notebooks/
│  └─ 01_train.ipynb
├─ src/
│  ├─ __init__.py
│  └─ utils.py
├─ tests/
│  └─ test_smoke.py
├─ .github/
│  ├─ workflows/
│  │  └─ run-notebook.yml
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ bug_report.md
│  │  └─ feature_request.md
│  └─ pull_request_template.md
├─ .devcontainer/
│  └─ devcontainer.json
├─ .editorconfig
├─ .gitignore
├─ CHANGELOG.md
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ LICENSE
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

## Colab GPU

- **Runtime → Change runtime type → GPU**
- Check GPU with:
  ```python
  !nvidia-smi
  ```

## Agentic Workflow

The core workflow combines local development, AI-assisted coding, and cloud GPU execution:

```
┌─────────────────────────────────────────────────────────────────┐
│  1. Copy Mission from AGENT_MISSIONS.md                         │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│  2. Paste into GitHub Copilot Chat (⌘ + i)                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│  3. Copilot Analyzes & Proposes Changes → Creates PR             │
│     (updates src/, tests/, notebooks/, README, requirements.txt)│
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│  4. Review PR in GitHub                                         │
│     (GitHub Actions runs smoke test on CPU)                    │
└────────────────────────┬────────────────────────────────────────┘
                         │
                    ✅ Approved?
                    │
┌────────────────────▼────────────────────────────────────────────┐
│  5. Merge to main                                               │
└────────────────────┬─────────────────────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────────────────────┐
│  6. Click Colab Badge in README                                  │
│     → Opens notebook in Google Colab                             │
└────────────────────┬─────────────────────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────────────────────┐
│  7. Set Runtime to GPU (T4, A100, etc.)                          │
│     → Run all cells on GPU                                       │
│     → Outputs saved to outputs/ folder                           │
└─────────────────────────────────────────────────────────────────┘
```

### Key Points

- **Develop locally** with GitHub Copilot Chat
- **PR review** ensures quality
- **Automated smoke test** on every PR
- **Colab GPU** for heavy lifting
- **Template repo** → Fork for new projects

## Getting Started

See these guides for step-by-step instructions:

- **Quick start**: [QUICK_REFERENCE.md](QUICK_REFERENCE.md) (5 min)
- **GitHub setup**: [GITHUB_PUSH_INSTRUCTIONS.md](GITHUB_PUSH_INSTRUCTIONS.md)
- **Colab GPU**: [COLAB_GPU_GUIDE.md](COLAB_GPU_GUIDE.md)
- **First mission**: [FIRST_MISSION.md](FIRST_MISSION.md) → Paste into Copilot Chat
- **All missions**: [AGENT_MISSIONS.md](AGENT_MISSIONS.md) (8 ready-to-use templates)

## License

MIT License — see [LICENSE](LICENSE) for details.
