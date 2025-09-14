"""
Image processing utilities for the CNC Pen Plotter application.
"""
import numpy as np
import cv2
from PIL import Image


def apply_filters(img, brightness, contrast, threshold, invert, edge_method):
    """Apply image processing filters."""
    # Convert PIL to numpy
    img_array = np.array(img)

    # Apply brightness and contrast
    img_array = cv2.convertScaleAbs(img_array, alpha=1 + contrast / 100, beta=brightness)

    # Apply edge detection
    if edge_method == 'canny':
        img_array = cv2.Canny(img_array, threshold, threshold * 2)
    elif edge_method == 'sobel':
        sobelx = cv2.Sobel(img_array, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(img_array, cv2.CV_64F, 0, 1, ksize=3)
        img_array = np.sqrt(sobelx ** 2 + sobely ** 2).astype(np.uint8)
    elif edge_method == 'laplacian':
        img_array = cv2.Laplacian(img_array, cv2.CV_64F)
        img_array = np.absolute(img_array).astype(np.uint8)

    # Apply threshold
    _, img_array = cv2.threshold(img_array, threshold, 255, cv2.THRESH_BINARY)

    # Invert if needed
    if invert:
        img_array = 255 - img_array

    return Image.fromarray(img_array, mode='L')


def extract_paths(img, method):
    """Extract vector paths from image."""
    # Mock implementation - returns dummy paths
    # In real implementation, this would use cv2.findContours, etc.
    return [(0, 0), (100, 100), (200, 50)] * 10