# Copilot Agent Missions (Templates)

These are ready-to-use prompts for GitHub Copilot Chat/Agents. Copy and paste them into the Copilot Chat panel to get started!

---

## 🎯 Mission 1: Add CIFAR-10 training pipeline

```
I want to add a CIFAR-10 training pipeline to this repo.

Here's what I need:
- Inspect `notebooks/01_train.ipynb` and `src/utils.py`
- Implement a clean CIFAR-10 pipeline with:
  - Dataset loading & transforms (via torchvision)
  - Simple CNN model
  - Train/validation loop with loss tracking
  - Log metrics to `outputs/metrics.csv` (epoch, loss, accuracy)
- Keep dependencies minimal (torch, torchvision, numpy, pandas)
- Add unit tests in `tests/test_smoke.py` for new utility functions
- Add a new notebook cell that demonstrates the pipeline
- Open a PR with a summary of changes

Focus on clean, readable code that's easy to modify for other datasets.
```

---

## 🎯 Mission 2: Optimize for A100 GPUs

```
I want to optimize the training code for A100 GPUs.

Here's what I need:
- Review the training loop in `notebooks/01_train.ipynb`
- Implement mixed precision training using `torch.cuda.amp` (AMP)
- Support larger batch sizes (configurable via environment variable `BATCH_SIZE`)
- Add a notebook cell that prints detailed GPU properties: `torch.cuda.get_device_properties(0)`
- Benchmark the difference in throughput/memory with and without mixed precision
- Update `README.md` with a brief performance note about A100 optimization
- Open a PR with the optimizations and benchmark results
```

---

## 🎯 Mission 3: Add data augmentation & regularization

```
I want to improve model robustness with augmentation and regularization.

Here's what I need:
- Add a `src/augmentation.py` module with:
  - Standard augmentation pipeline (RandomCrop, RandomHorizontalFlip, ColorJitter, etc.)
  - Function to create train/val augmentation pipelines
- Implement L2 regularization in the training loop (configurable weight decay)
- Add dropout layers to the CNN model
- Create a new notebook cell comparing metrics with/without augmentation
- Add tests in `tests/` to validate augmentation outputs
- Open a PR with documentation of the augmentation strategy
```

---

## 🎯 Mission 4: Add distributed training support

```
I want to add multi-GPU support using PyTorch Distributed Data Parallel.

Here's what I need:
- Refactor the training loop in `src/train.py` to support DDP
- Add environment variable configuration for distributed setup
- Create a notebook cell that demonstrates DDP training
- Keep backward compatibility (single GPU should still work)
- Add a brief guide in `CONTRIBUTING.md` about running distributed training
- Open a PR with the distributed training implementation

Focus on making it easy for users to run on multi-GPU Colab Pro setups.
```

---

## 🎯 Mission 5: Add model checkpointing & resumption

```
I want to add checkpointing and training resumption.

Here's what I need:
- Implement `save_checkpoint()` and `load_checkpoint()` in `src/utils.py`
- Save: model state, optimizer state, epoch, loss history
- Add a notebook cell that demonstrates checkpoint saving every N epochs
- Implement training resumption from the latest checkpoint
- Save checkpoints to `checkpoints/` folder
- Add a utility to list available checkpoints
- Update `.gitignore` if needed
- Open a PR with checkpoint utilities and usage examples
```

---

## 🎯 Mission 6: Add experiment tracking (Weights & Biases)

```
I want to add experiment tracking with Weights & Biases (wandb).

Here's what I need:
- Add wandb to `requirements.txt`
- Create a `src/wandb_logger.py` module for experiment tracking
- Integrate wandb into the training loop in the notebook
- Log: loss, accuracy, learning rate, GPU memory usage
- Add a configuration section in the notebook for wandb project/entity
- Include instructions in `README.md` for setting up wandb API key in Colab
- Make wandb integration optional (graceful degradation if not configured)
- Open a PR with the wandb integration and usage docs
```

---

## 🎯 Mission 7: Add Lora fine-tuning for pretrained models

```
I want to add LoRA (Low-Rank Adaptation) fine-tuning for transfer learning.

Here's what I need:
- Add `peft` library to `requirements.txt`
- Create `src/lora_utils.py` with LoRA configuration helpers
- Implement functions to convert a pretrained model (e.g., ResNet) to LoRA
- Add a notebook cell demonstrating LoRA fine-tuning on a custom dataset
- Log trainable parameters count (base model vs LoRA)
- Add tests for LoRA utilities
- Update `README.md` with a brief explanation of LoRA
- Open a PR with LoRA implementation
```

---

## 🎯 Mission 8: Add evaluation & test set metrics

```
I want to add comprehensive evaluation on a held-out test set.

Here's what I need:
- Refactor the training loop to separate train/val/test phases
- Compute and log: accuracy, precision, recall, F1, confusion matrix
- Save evaluation results to `outputs/evaluation.json` with detailed metrics
- Create a notebook cell that loads the best checkpoint and runs evaluation
- Add helper functions in `src/eval.py` to compute metrics
- Generate and save a confusion matrix plot to `outputs/confusion_matrix.png`
- Add tests for the evaluation metrics
- Open a PR with the evaluation framework
```

---

## 📌 Tips

1. **Copy a mission** → Paste into Copilot Chat
2. **Copilot will**:
   - Analyze the existing codebase
   - Generate/modify files as needed
   - Suggest PR changes
3. **Review the PR** → Merge when ready
4. **Run tests locally**: `pytest -q`
5. **Test in Colab**: Open the notebook in Colab GPU runtime

---

## 🚀 Creating your own missions

Use this template:

```
I want to [high-level goal].

Here's what I need:
- [Specific file changes or new files]
- [Behavior or functionality]
- [Tests or validation]
- [Documentation updates]
- Open a PR with [summary]

Focus on [key considerations].
```

Happy collaborating! 🎉
