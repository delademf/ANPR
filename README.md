# ANPR
Automatic Number Plate Recognition(Optical Character Recognition (OCR) and Text Annotation with OpenCV and EasyOCR)

This repository contains Python code for performing Optical Character Recognition (OCR) on images using the EasyOCR library and annotating the detected text on the original image. Additionally, it demonstrates some common image processing techniques using OpenCV.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

Optical Character Recognition (OCR) is a technology that enables the recognition of text within images. This repository showcases a simple Python script that performs OCR on an image, detects text, and annotates it on the original image using OpenCV and the EasyOCR library.

## Prerequisites

Before you get started, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- EasyOCR
- Matplotlib

You can install the required Python libraries using `pip`. For example:

```bash
pip install opencv-python-headless
pip install numpy
pip install easyocr
pip install matplotlib
```

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/ANPR.git
```

2. Change your current directory to the project folder:

```bash
cd ANPR
```

## Usage

1. Place your image in the `images` directory.

2. Update the `img` variable with the filename of your image:

```python
img = cv.imread('images/your-image.jpg')
```

3. Run the Python script:

```bash
python ocr_and_annotation.py
```

The script will perform the following steps:

- Load the image.
- Apply image processing techniques, including rescaling, edge detection, and contour analysis.
- Perform OCR on the detected text using EasyOCR.
- Annotate the text on the original image.
- Display the annotated image with detected text.

4. You can press any key to close the displayed image and view the annotated result.

## License

This code is provided under the [MIT License](LICENSE).

---
