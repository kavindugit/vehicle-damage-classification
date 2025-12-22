"""import streamlit as st
from model_helper import predict
st.title("Vehical Damage Detection")
uploaded_file = st.file_uploader("Upload an image of the vehicle", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    prediction = predict(image_path)
    st.info(f"Predicted class : {prediction}")"""
import streamlit as st
from model_helper import predict
from PIL import Image
import tempfile

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader(
    "Upload an image of the vehicle",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Display image safely
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Create a temporary file (cloud-safe)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_path = tmp.name

    # Prediction
    prediction = predict(temp_path)
    st.info(f"Predicted class: {prediction}")
