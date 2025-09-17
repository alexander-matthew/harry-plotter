"""Generative art utilities for the CNC Pen Plotter application."""
from __future__ import annotations

import logging

import cv2
import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)


def generate_art(algorithm: str, complexity: int, scale: float) -> Image.Image:
    """Generate procedural art based on selected algorithm."""
    size = int(200 * scale)

    if algorithm == 'flow_field':
        img = np.zeros((size, size))
        for _ in range(complexity * 10):
            x = np.random.randint(0, size)
            y = np.random.randint(0, size)
            length = np.random.randint(10, 50)
            angle = np.random.random() * 2 * np.pi
            for j in range(length):
                x_new = int(x + j * np.cos(angle))
                y_new = int(y + j * np.sin(angle))
                if 0 <= x_new < size and 0 <= y_new < size:
                    img[y_new, x_new] = 255
                angle += np.random.randn() * 0.3

    elif algorithm == 'spirograph':
        img = np.zeros((size, size))
        t = np.linspace(0, complexity * 2 * np.pi, 1000 * complexity)
        R, r, d = 50 * scale, 30 * scale, 40 * scale
        x = (R - r) * np.cos(t) + d * np.cos((R - r) * t / r)
        y = (R - r) * np.sin(t) - d * np.sin((R - r) * t / r)
        x = ((x - x.min()) / (x.max() - x.min()) * (size - 20) + 10).astype(int)
        y = ((y - y.min()) / (y.max() - y.min()) * (size - 20) + 10).astype(int)
        for i in range(len(x) - 1):
            cv2.line(img, (x[i], y[i]), (x[i + 1], y[i + 1]), 255, 1)

    elif algorithm == 'voronoi':
        img = np.zeros((size, size))
        points = np.random.rand(complexity * 5, 2) * size
        for y in range(size):
            for x in range(size):
                distances = np.sqrt((points[:, 0] - x) ** 2 + (points[:, 1] - y) ** 2)
                if np.min(distances) < 3:
                    img[y, x] = 255

    elif algorithm == 'circle_packing':
        img = np.zeros((size, size))
        for _ in range(complexity * 20):
            x, y = np.random.randint(10, size - 10), np.random.randint(10, size - 10)
            r = np.random.randint(5, 20)
            cv2.circle(img, (x, y), r, 255, 1)
    else:
        img = np.random.rand(size, size) * 255

    logger.debug("Generated %s art with complexity=%s scale=%s", algorithm, complexity, scale)
    return Image.fromarray(img.astype(np.uint8), mode='L')
