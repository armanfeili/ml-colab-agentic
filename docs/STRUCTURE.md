# Docs Folder Structure Guide

This guide explains where Copilot-generated documentation should go.

## Folder Organization

### 📖 `docs/guides/`

Quick references and how-to guides for users

**Place here when Copilot generates:**

- Quick start guides
- Tutorial walkthroughs
- Best practices
- Troubleshooting guides
- Tool usage guides (ruff, black, pytest)

**Example files:**

- `QUICK_REFERENCE.md`
- `COLAB_GPU_GUIDE.md`
- `TIPS_AND_TRICKS.md` (future)
- `TROUBLESHOOTING.md` (future)

### 🔧 `docs/setup/`
**Deployment, configuration, and installation**

*Place here when Copilot generates:*
- Installation instructions
- Environment setup
- GitHub configuration
- Deployment guides
- Docker/container setup
- Configuration checklists

*Example files:*
- `GITHUB_PUSH_INSTRUCTIONS.md`
- `GITHUB_SETTINGS_GUIDE.md`
- `SETUP_COMPLETE.md`
- `FINAL_CHECKLIST.md`
- `DOCKER_SETUP.md` (future)
- `ENVIRONMENT_SETUP.md` (future)

### 🤖 `docs/missions/`
**Copilot Agent missions and agentic workflows**

*Place here when Copilot generates:*
- Agent missions (copy-paste into Copilot Chat)
- Mission collections
- Workflow templates
- Task automation guides
- Refactoring guides

*Example files:*
- `FIRST_MISSION.md`
- `AGENT_MISSIONS.md`
- `ADVANCED_MISSIONS.md` (future)
- `REFACTORING_WORKFLOWS.md` (future)

### 🔄 `docs/workflows/`
**CI/CD, GitHub Actions, and deployment workflows**

*Place here when Copilot generates:*
- GitHub Actions workflow documentation
- CI/CD pipeline guides
- Automated deployment docs
- Testing workflows
- Release processes

*Example files:*
- `GITHUB_ACTIONS.md` (future)
- `CI_CD_PIPELINE.md` (future)
- `DEPLOYMENT_WORKFLOW.md` (future)
- `TESTING_STRATEGY.md` (future)

### 🔌 `docs/api/`
**API reference and utility documentation**

*Place here when Copilot generates:*
- Module API documentation
- Function reference
- Class documentation
- Type hints reference
- Configuration reference

*Example files:*
- `UTILS_API.md` (future)
- `CONFIG_REFERENCE.md` (future)
- `FUNCTIONS.md` (future)
- `CLASSES.md` (future)

---

## File Naming Conventions

Follow these patterns for consistency:

```
🔤 Type                    📝 Pattern
─────────────────────────────────────────
Quick guides              NOUN_GUIDE.md
Setup instructions        SETUP_NOUN.md
Step-by-step             HOW_TO_NOUN.md
Reference docs           NOUN_REFERENCE.md
Collections              NOUN_COLLECTION.md
API docs                 NOUN_API.md
Examples                 NOUN_EXAMPLES.md
Troubleshooting          TROUBLESHOOTING_NOUN.md
```

Examples:
- `docs/guides/GPU_GUIDE.md`
- `docs/setup/DOCKER_SETUP.md`
- `docs/missions/ADVANCED_MISSIONS.md`
- `docs/workflows/GITHUB_ACTIONS.md`
- `docs/api/UTILS_API.md`

---

## Documentation Template (for Copilot)

When asking Copilot to generate documentation, use this template:

```markdown
# [Title]

[Brief description - 1-2 sentences]

## Overview

[What is this? Why is it important?]

## Getting Started

[Step-by-step instructions]

## Examples

[Code examples or usage examples]

## Advanced Usage

[More complex scenarios]

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Issue 1 | Solution 1 |

## Related Docs

- [Link to related doc](path/to/doc.md)
- [Link to related doc](path/to/doc.md)

## See Also

- [External link](url)
```

---

## When Copilot Generates New Docs

**Ask Copilot to:**

1. **Determine the category:**
   - Is it a how-to? → `docs/guides/`
   - Is it setup? → `docs/setup/`
   - Is it a mission? → `docs/missions/`
   - Is it CI/CD? → `docs/workflows/`
   - Is it API ref? → `docs/api/`

2. **Follow naming convention:**
   - Use the patterns above
   - Keep names descriptive but concise
   - Use underscores for multi-word names

3. **Create with context:**
   ```
   "Create a new guide in docs/guides/ called 
   HOW_TO_DISTRIBUTED_TRAINING.md that explains 
   multi-GPU setup with PyTorch DDP. 
   Include examples and troubleshooting."
   ```

4. **Update README if needed:**
   - Update `docs/README.md` to reference new file
   - Update `README.md` if it's a major guide

---

## Maintenance

**Quarterly review:**
- [ ] Check for outdated docs
- [ ] Move misplaced files to correct folder
- [ ] Update index in `docs/README.md`
- [ ] Remove deprecated docs (archive first)

**When moving docs:**
- Update all links pointing to moved files
- Add redirect note in old location if keeping file
- Update `docs/README.md` index

---

## Examples

### Adding a new GPU optimization guide

```bash
# Create the file
touch docs/guides/GPU_OPTIMIZATION.md

# Ask Copilot:
# "Write a comprehensive guide to GPU optimization for PyTorch 
# in docs/guides/GPU_OPTIMIZATION.md. Include mixed precision, 
# gradient accumulation, and batch size tuning. Add examples 
# and performance benchmarks."

# Update index
# Edit docs/README.md to add entry under guides/
```

### Adding a Docker deployment guide

```bash
# Create the file
touch docs/setup/DOCKER_DEPLOYMENT.md

# Ask Copilot:
# "Write setup guide for Docker deployment in 
# docs/setup/DOCKER_DEPLOYMENT.md. Include Dockerfile 
# creation, Docker Compose setup, and registry pushing."

# Update index
# Edit docs/README.md to add entry under setup/
```

### Adding new advanced missions

```bash
# Create the file
touch docs/missions/ADVANCED_MISSIONS.md

# Ask Copilot:
# "Create 3 advanced Copilot Agent missions in 
# docs/missions/ADVANCED_MISSIONS.md for: 
# 1) Multi-modal training pipeline, 
# 2) AutoML hyperparameter tuning, 
# 3) Model quantization for inference. 
# Follow the format of AGENT_MISSIONS.md."

# Update index
# Edit docs/README.md and update missions section
```

---

## Summary

```
docs/
├── guides/        👈 How-to, tips, troubleshooting
├── setup/         👈 Installation, configuration, deployment
├── missions/      👈 Copilot Agent missions
├── workflows/     👈 CI/CD, GitHub Actions
├── api/           👈 API reference, class/function docs
└── README.md      👈 Documentation index (update when adding files!)
```

**Rule of thumb:** When in doubt, start with the folder name that best describes the content type, not the topic.

- "How do I...?" → `guides/`
- "How do I set up...?" → `setup/`
- "How do I use Copilot to...?" → `missions/`
- "How does the automation...?" → `workflows/`
- "What does this function do...?" → `api/`

---

For questions about documentation organization, see [../CONTRIBUTING.md](../CONTRIBUTING.md)
