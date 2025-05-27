import streamlit as st
import os

# Path to the folder containing images
image_folder = "1"

# Get image filenames sorted
images = sorted([img for img in os.listdir(image_folder) if img.lower().endswith(('.jpg', '.jpeg', '.png'))])

# Set page layout
st.set_page_config(layout="centered")

# Custom styling
st.markdown("""
    <style>
    .carousel-img {
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.3s ease, opacity 0.3s ease;
    }
    .center {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize index
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Navigation controls
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("◀️", use_container_width=True):
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1

with col3:
    if st.button("▶️", use_container_width=True):
        if st.session_state.current_index < len(images) - 1:
            st.session_state.current_index += 1

# Display the current image
current_image = os.path.join(image_folder, images[st.session_state.current_index])
with col2:
    st.image(current_image, use_container_width=True, caption=images[st.session_state.current_index])

# Optional counter
st.markdown(
    f"<p style='text-align:center; color:white;'>Image {st.session_state.current_index + 1} of {len(images)}</p>",
    unsafe_allow_html=True
)
