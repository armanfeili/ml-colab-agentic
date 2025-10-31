"""Utility functions for training and device management."""

from __future__ import annotations

import os
import random

import numpy as np
import torch


def set_seed(seed: int = 42) -> None:
  """Set random seed for reproducibility across numpy, torch, and CUDA.

  Args:
    seed: Random seed value (default: 42).
  """
  random.seed(seed)
  np.random.seed(seed)
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)
  # Ensure deterministic behavior for CUDA operations
  os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"


def to_device(x, device=None):
  """Move tensor or model to the specified device.

  Args:
    x: Tensor or model to move.
    device: Target device (default: CUDA if available, else CPU).

  Returns:
    Moved tensor or model.
  """
  device = device or ("cuda" if torch.cuda.is_available() else "cpu")
  if hasattr(x, "to"):
    return x.to(device)
  return x
