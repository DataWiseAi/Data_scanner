import streamlit as st
import pytesseract
import cv2
from PIL import Image
import numpy as np

myconfig = r"--psm 11 --oem 3"

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

        # Perform text detection and draw bounding boxes
        boxes = pytesseract.image_to_boxes(img_cv, config=myconfig)
        for box in boxes.splitlines():
            box = box.split(" ")
            img_cv = cv2.rectangle(img_cv, (int(box[1]), height - int(box[2])),
                                    (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

        # Display the image with bounding boxes
        st.image(img_cv, caption="Text Detection with Bounding Boxes", use_column_width=True)

if __name__ == "__main__":
    main()
