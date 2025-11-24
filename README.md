# Task7_Elevate_Labs
Sure, Naveen — here’s a clean, polished, GitHub-ready **README.md** for your *Image Resizer Tool* project. It’s simple, professional, and actually looks like something you'd see in a real repository.

---

# 📸 Image Resizer Tool

*A simple, reliable batch image resizer built with Python and Pillow.*

---

## 🚀 Overview

Managing large sets of images manually is a pain — especially when they’re all different sizes. This tool automates that job.
Just point it to a folder, set your preferred width & height, and the script resizes **every image** in one go.

Perfect for web optimization, dataset preprocessing, or cleaning up messy photo collections.

---

## ✨ Features

* 🔄 **Batch Resize** — processes all images in a directory
* 📁 **Folder-Based Automation** — no manual image selection
* 🖼️ **Supports JPG, PNG, JPEG, and more**
* 🔧 **Easy to Customize** — tweak size, format, or output folder
* 💡 **Lightweight** — minimal dependencies (only Pillow)

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Pillow (PIL)**

---

## 📂 Project Structure

```
Image-Resizer-Tool/
│── images/            # Input folder
│── output/            # Resized images (auto-created)
│── resize.py          # Main script
│── README.md
```

---

## ▶️ How to Use

### 1️⃣ Install Dependencies

```bash
pip install pillow
```

### 2️⃣ Place Images

Put all the images you want to resize in the `images/` folder.

### 3️⃣ Run the Script

```bash
python resize.py
```

### 4️⃣ Get Output

All resized images appear inside the `output/` folder automatically.

---


## 🌱 Future Improvements

* Add CLI arguments (`--width --height --format`)
* Add bulk format converter
* Add GUI using Tkinter or PyQt
* Add progress bar (tqdm)

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas to improve or extend the tool, feel free to open an issue.

---

