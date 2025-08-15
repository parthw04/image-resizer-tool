# 🖼️ Image Resizer Tool

A simple **Python + Pillow** script that resizes and converts images in bulk.  
This tool automates image resizing tasks for any folder of images.

---

## 📌 Features
- Resize all images in a folder to your desired dimensions.
- Convert images to JPG, PNG, or WEBP.
- Automatically creates the output folder if it doesn’t exist.
- Skips non-image files.

---

## ⚙️ Requirements
- Python 3.x
- Pillow library

Install dependencies:
```bash
pip install pillow
```
---
## 🚀 How to Use

1. Clone the repository

2. git clone https://github.com/parthw04/image-resizer-tool.git
3. cd image-resizer-tool


### Run the script

```python image_resizer.py```

Enter details when prompted:

```Path to input folder (where your images are stored)

Path to output folder (where resized images will be saved)

New width (in pixels)

New height (in pixels)

Output format (jpg, png, webp — or leave blank to keep original format)
```
---

## 📂 Example
Enter the path to the input folder: input_images
Enter the path to the output folder: resized_images
Enter new width (px): 800
Enter new height (px): 600
Enter output format (jpg/png/webp, leave blank to keep original): jpg
