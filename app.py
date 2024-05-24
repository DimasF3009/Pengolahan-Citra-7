import streamlit as st
import matplotlib.pyplot as plt
from skimage.morphology import convex_hull_image
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
from PIL import Image
import numpy as np

st.title("Convex Hull Transformation of an Image")

# Upload file image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Membaca gambar kucing dari direktori lokal dan konversi ke RGB
    image = Image.open(uploaded_file).convert('RGB') 

    # Konversi gambar PIL ke array numpy
    image= np.array(image)

    # Konversi gambar ke grayscale dan invert warnanya
    image_gray = rgb2gray(image)
    image_inverted = invert(image_gray)

    # Menerapkan convex hull
    chull = convex_hull_image(image_inverted)

    # Plotting gambar asli dan hasil transformasi convex hull
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()

    ax[0].set_title('original')
    ax[0].imshow(image_gray, cmap=plt.cm.gray)
    ax[0].set_axis_off()

    ax[1].set_title('transformed')
    ax[1].imshow(chull, cmap=plt.cm.gray)
    ax[1].set_axis_off()

    plt.tight_layout()
    st.pyplot(fig)

