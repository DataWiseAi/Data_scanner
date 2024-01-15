import streamlit as st
import cv2
from PIL import Image
import numpy as np
import easyocr

def main():
    st.title("Text Detection and Bounding Boxes App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert the image to OpenCV format
        img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        height, width, _ = img_cv.shape

        # Perform text detection and draw bounding boxes using easyocr with GPU acceleration
        reader = easyocr.Reader(['en'], gpu=True)  # Enable GPU acceleration
        results = reader.readtext(img_cv)

        # Draw bounding boxes on the image
        for result in results:
            points = result[0]
            box = np.array(points).astype(np.int32).reshape((-1, 1, 2))
            img_cv = cv2.polylines(img_cv, [box], isClosed=True, color=(0, 255, 0), thickness=2)

        # Display the image with bounding boxes
        st.image(img_cv, caption="Text Detection with Bounding Boxes", use_column_width=True)

if __name__ == "__main__":
    main()
