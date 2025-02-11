import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import os

# Set up the Streamlit page configuration
st.set_page_config(layout="wide", page_title="Image Background Remover")

# CSS for the header and text styling
st.markdown(
    """
    <style>
    .header {
        background-color: #6a0dad; /* Purple background */
        color: white; /* White text color */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 36px; /* Large font size for the header */
    }
    .description {
        background-color: #f5f5f5; /* Light gray background for description */
        color: #333; /* Dark text color */
        padding: 20px;
        border-radius: 10px;
        margin-top: 30px; /* Space between header and description */
        text-align: center;
        font-size: 18px; /* Font size for the description */
        line-height: 1.6; /* Line height for better readability */
    }
    .description a {
        color: #6a0dad; /* Purple color for the link */
        text-decoration: none; /* Remove underline from link */
        font-weight: bold; /* Make the link bold */
    }
    .description a:hover {
        text-decoration: underline; /* Add underline on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and description styling
st.markdown(
    """
    <div class="header">
        Remove background from your image
    </div>
    <div class="description">
        🐾 Upload an image and see the background vanish like magic! 
        Download the high-quality result from the sidebar. 
        This project is open source and available <a href="https://github.com/Abdisamad001/BG_Removal/tree/main" target="_blank">here</a> on GitHub.
    </div>
    """,
    unsafe_allow_html=True
)

# File size limit
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Cache image conversion to optimize performance
@st.cache_data
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG", optimize=True, quality=100)
    byte_im = buf.getvalue()
    return byte_im

# Cache background removal process
@st.cache_data
def fix_image(upload):
    image = Image.open(upload)
    fixed = remove(image)
    return image, fixed

# Sidebar for file upload and download
st.sidebar.write("## Upload and download :gear:")
uploaded_image = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Display a static GIF if no image is uploaded
center_gif_path = "center.gif"
default_gif = open(center_gif_path, "rb").read() if os.path.exists(center_gif_path) else None

# Layout for original and processed images
col1, col2 = st.columns([1, 1])

if uploaded_image is not None:
    if uploaded_image.getbuffer().nbytes > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        with st.spinner("Processing image..."):
            try:
                original, fixed = fix_image(upload=uploaded_image)
                col1.write("Original Image :camera:")
                col1.image(original, use_container_width=True)
                col2.write("Removed Background :wrench:")
                col2.image(fixed, use_container_width=True)

                # Sidebar download button
                st.sidebar.download_button("Download image", convert_image(fixed), "fixed.png", "image/png")
            except Exception as e:
                st.error(f"An error occurred: {e}")
elif default_gif:
    st.image(default_gif, use_container_width=True)
else:
    st.write("Upload an image to start removing its background.")
