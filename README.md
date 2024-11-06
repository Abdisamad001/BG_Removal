# Image Background Remover

A powerful and user-friendly web application built with Streamlit that automatically removes backgrounds from images using advanced computer vision techniques.

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-3.8.0-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.25.0-red)
![rembg](https://img.shields.io/badge/rembg-2.0.30-green)
![Pillow](https://img.shields.io/badge/Pillow-9.4.0-yellow)
![numba](https://img.shields.io/badge/numba-0.57.1-orange)
![numpy](https://img.shields.io/badge/numpy-1.23.5-blue)

## 🌐 Live Demo
Got to the website: [Background Remover App](https://bgremoval-ayu6dnqt5uaefyj9kyh63c.streamlit.app/)

## 🚀 Features

- **One-Click Background Removal**: Simple drag-and-drop interface
- **High Resolution Support**: Process images up to 200MB
- **Multiple Format Support**: Handles PNG, JPG, and JPEG files
- **Instant Preview**: See results in real-time
- **High-Quality Output**: Maintains image quality after background removal
- **Easy Download**: Quick download of processed images

## 🛠️ Technical Requirements

### Python Version
- Python 3.8.0

### Dependencies
```bash
rembg==2.0.30
Pillow==9.4.0
streamlit==1.25.0
numba==0.57.1
numpy==1.23.5

🔧 Installation
Clone the repository:

git clone https://github.com/Abdisamad001/BG_Removal.git
cd BG_Removal

Set up Conda environment:
# Create new conda environment
conda create -p venv python==3.8.0 -y

# Activate the environment
conda activate ./venv

Install required packages:
pip install rembg==2.0.30 Pillow==9.4.0 streamlit==1.25.0 numba==0.57.1 numpy==1.23.5

# Or use requirements.txt
pip install -r requirements.txt

Run the application:
streamlit run app.py

Alternative Environment Setup (if not using Conda)
Using venv:
#### Windows
python -m venv venv
.\venv\Scripts\activate

#### Linux/Mac
python -m venv venv
source venv/bin/activate


💻 Application Interface
The application features a clean, user-friendly interface with:
A centered heading "Remove background from your image"
Drag and drop file upload area
File size limit of 200MB
Supported formats: PNG, JPG, JPEG
Download option in the sidebar


⚡ Performance Notes
Optimized for images up to 200MB
Processing time depends on:
Image size
Image complexity
System specifications
Available memory

📝 License
This project is licensed under the MIT License - see the LICENSE file for details

💬 Contact
Abdisamad Omar - @LinkedIn


