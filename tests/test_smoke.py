"""Smoke tests for core utilities."""

import numpy as np
import torch

from src.utils import set_seed, to_device


def test_imports():
  """Test that all core imports work."""
  import numpy  # noqa: F401
  import pandas  # noqa: F401
  import torch  # noqa: F401


def test_set_seed():
  """Test that set_seed produces reproducible results."""
  set_seed(0)
  x1 = torch.randn(2, 2)

  set_seed(0)
  x2 = torch.randn(2, 2)

  assert torch.allclose(x1, x2), "Seed did not produce reproducible results"


def test_to_device():
  """Test that to_device moves tensors correctly."""
  set_seed(0)
  x = torch.randn(2, 2)
  y = to_device(x)

  assert y.shape == (2, 2), "Tensor shape changed"
  assert y.device.type in ["cuda", "cpu"], f"Unexpected device: {y.device}"


def test_torch_basic():
  """Test basic PyTorch functionality."""
  set_seed(0)
  x = torch.randn(3, 3)
  y = x @ x.T
  assert y.shape == (3, 3), "Matrix multiplication failed"
