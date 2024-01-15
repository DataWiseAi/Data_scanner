import easyocr
import streamlit as st
from PIL import Image

# Create the Reader instance outside the main function
reader = easyocr.Reader(['en'])

def main():
    st.title("Image Text Extraction App")

    allowed_extensions = ["jpg", "jpeg", "png", "gif"]
    uploaded_file = st.file_uploader("Choose an image...", type=allowed_extensions)

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform text extraction using easyocr
        results = reader.readtext(image)

        # Extracted text
        text = " ".join(result[1] for result in results)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text(text)

if __name__ == "__main__":
    main()
