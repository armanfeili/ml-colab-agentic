# data/

Datasets are not committed to this repository.

## In Colab

Mount Google Drive and read from:

```
/content/drive/MyDrive/...
```

Or download datasets directly to `/content/data`:

```python
import torchvision.datasets as datasets
datasets.CIFAR10(root="/content/data", train=True, download=True)
```

This folder (after downloading) will be ignored by git.
