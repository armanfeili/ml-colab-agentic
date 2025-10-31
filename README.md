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

## Agentic workflow

- Use Copilot Chat/Agents to propose edits → create PRs.
- Merge PRs → open notebook in Colab → run on GPU.

## License

MIT License — see [LICENSE](LICENSE) for details.
