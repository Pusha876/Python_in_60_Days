import streamlit as st
from PIL import Image

st.subheader("Color to GrayScale Converter")

# Create a file uploader component allowing the user to upload an image file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    st.write("This is a camera expander")
    st.write("You can take a picture using the camera")

    # Start the camera
    camera_image = st.camera_input("Camera")

    if camera_image:
        # Create a pillow image instance
        img = Image.open(camera_image)

        # Convert the pillow image to grayscale
        gray_img = img.convert('L')

        # Render the grayscale image on the webpage
        st.image(gray_img)
