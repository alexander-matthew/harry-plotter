"""Image processing utilities for the CNC Pen Plotter application."""
from __future__ import annotations

import logging
from typing import List, Tuple

import cv2
import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)


def apply_filters(
    img: Image.Image,
    brightness: int,
    contrast: int,
    threshold: int,
    invert: bool,
    edge_method: str,
) -> Image.Image:
    """Apply image processing filters."""
    img_array = np.array(img)
    img_array = cv2.convertScaleAbs(img_array, alpha=1 + contrast / 100, beta=brightness)

    if edge_method == 'canny':
        img_array = cv2.Canny(img_array, threshold, threshold * 2)
    elif edge_method == 'sobel':
        sobelx = cv2.Sobel(img_array, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(img_array, cv2.CV_64F, 0, 1, ksize=3)
        img_array = np.sqrt(sobelx ** 2 + sobely ** 2).astype(np.uint8)
    elif edge_method == 'laplacian':
        img_array = cv2.Laplacian(img_array, cv2.CV_64F)
        img_array = np.absolute(img_array).astype(np.uint8)

    _, img_array = cv2.threshold(img_array, threshold, 255, cv2.THRESH_BINARY)

    if invert:
        img_array = 255 - img_array

    return Image.fromarray(img_array, mode='L')


def extract_paths(img: Image.Image, method: str) -> List[Tuple[int, int]]:
    """Extract vector paths from image.

    TODO: Implement real path extraction using cv2.findContours or similar.
    """
    raise NotImplementedError("Path extraction not implemented")
