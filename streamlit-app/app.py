import streamlit as st
from model_helper import predict
st.title("Vehical Damage Detection")
uploaded_file = st.file_uploader("Upload an image of the vehicle", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    prediction = predict(image_path)
    st.info(f"Predicted class : {prediction}")