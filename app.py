import streamlit as st
from transformers import pipeline
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Smart Object Detector",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 Smart Object Detector")
st.write("Upload an image and AI will detect the objects in it.")

# Load object detection model
@st.cache_resource
def load_detector():
    return pipeline(
        "object-detection",
        model="facebook/detr-resnet-50"
    )

detector = load_detector()

# Upload image
uploaded_file = st.file_uploader(
    "📷 Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Uploaded Image")
    st.image(image, use_container_width=True)

    if st.button("🔍 Detect Objects", key="detect_button"):

        with st.spinner("Detecting objects..."):
            results = detector(image)

        st.subheader("🎯 Detected Objects")

        if results:
            for item in results:
                object_name = item["label"]
                confidence = item["score"]

                st.write(
                    f"**{object_name}** — "
                    f"Confidence: {confidence:.2%}"
                )
        else:
            st.info("No objects detected.")