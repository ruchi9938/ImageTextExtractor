# Image Text and Visual Element Extractor

This program separates text and visual elements from an image using image analysis, Optical Character Recognition (OCR), and basic image segmentation techniques. The extracted content is organized into an HTML file with appropriate tags for text and images.

## Features

- **Image Analysis**: Analyze the uploaded image to prepare it for text and visual element extraction.
- **Text Extraction**: Use Tesseract OCR to extract all text content from the image.
- **Visual Element Segmentation**: Apply edge detection and contour detection to isolate individual visual elements within the image.
- **HTML Generation**: Create a basic HTML structure to sort the extracted content into appropriate tags like paragraphs (`<p>`) and images (`<img>`).

## Requirements

- Python 3.x
- OpenCV
- Tesseract OCR
- Pillow
- NumPy
- pytesseract

## Installation

1. **Install Python Packages**:
   ```bash
   pip install opencv-python pytesseract Pillow numpy
