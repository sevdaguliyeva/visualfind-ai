
import streamlit as st
from PIL import Image

from model import find_object


st.set_page_config(
    page_title="VisualFind AI",
    page_icon="icon.png",
    layout="wide"
)

st.title("VisualFind AI")
st.write("Upload images and find objects using AI.")

uploaded_files = st.file_uploader(
    "Upload up to 10 images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

search_term = st.text_input(
    "Search for an object",
    placeholder="e.g. car, dog, bicycle"
)

if uploaded_files:
    if len(uploaded_files) > 10:
        st.error("You can upload a maximum of 10 images.")

    elif search_term.strip():
        if st.button("Search"):
            matching_images = []

            with st.spinner("Searching images..."):
                for uploaded_file in uploaded_files:
                    image = Image.open(uploaded_file).convert("RGB")

                    if find_object(image, search_term.strip()):
                        matching_images.append(
                            (uploaded_file.name, image)
                        )

            if matching_images:
                st.success(
                    f"Found {len(matching_images)} matching image(s)."
                )

                columns = st.columns(3)

                for index, (name, image) in enumerate(matching_images):
                    with columns[index % 3]:
                        st.image(image, caption=name, use_container_width=True)
            else:
                st.info("No matches found.")
