import streamlit as st

# page configurations
st.title("License Plate Detection Application")


# Upload image function
def upload_image():
    uploaded_file = st.file_uploader("Upload Image to extract the license plates", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        with st.spinner("Processing..."):
            # Save the uploaded image to a local file
            with open("uploaded_image.jpg", "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success("Image uploaded and stored successfully!")


# Upload video function
def upload_video():
    uploaded_file = st.file_uploader("Upload Video to extract the license plates", type=["mp4"])
    if uploaded_file is not None:
        with st.spinner("Processing..."):
            # Save the uploaded video to a local file
            with open("uploaded_video.mp4", "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success("Video uploaded and stored successfully!")


upload_image()
upload_video()


if st.button("Start Detection"):
    st.success("Detection started..!")
