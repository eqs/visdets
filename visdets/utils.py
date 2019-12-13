# -*- coding: utf-8 -*-
import numpy as np
import torch

__all__ = ['tensor2cvmat']


def tensor2cvmat(image: torch.Tensor) -> np.ndarray:
    return np.uint8(image.permute(1, 2, 0).numpy() * 255).copy()
