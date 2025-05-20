import streamlit as st
import os

def display_png(png_path):
    """
    Displays a PNG file in the Streamlit app.

    Args:
        png_path (str): The path to the PNG file.
    """
    st.image(png_path, use_container_width=True)

def main():
   

    # Folder containing PNG files
    png_folder = "pngs"
    png_files = sorted([png for png in os.listdir(png_folder) if png.lower().endswith(".png")])

    # Check if the folder exists
    if not os.path.exists(png_folder):
        st.error(f"Error: The folder '{png_folder}' does not exist. Please create it and put your PNG files there.")
        return

    # Check if there are any PNG files in the folder
    if not png_files:
        st.error(f"Error: The folder '{png_folder}' is empty or contains no PNG files.")
        return

    # Initialize session state
    if "png_index" not in st.session_state:
        st.session_state.png_index = 0
    if "left_clicked" not in st.session_state:  # Add this
        st.session_state.left_clicked = False
    if "right_clicked" not in st.session_state: # Add this
        st.session_state.right_clicked = False

    # Get the current PNG file path
    current_png = png_files[st.session_state.png_index]
    png_path = os.path.join(png_folder, current_png)

    # Display the current PNG
    display_png(png_path)

    # Create columns for clickable areas
    left_col, right_col = st.columns(2)

    # Use st.container() and st.markdown() to create clickable areas
    with left_col:
        if st.markdown("<div style='height: 600px;'></div>", unsafe_allow_html=True):
            if st.session_state.left_clicked: # Only change if left is clicked
                st.session_state.left_clicked = False #reset
                if st.session_state.png_index > 0:
                    st.session_state.png_index -= 1
                    st.rerun()

    with right_col:
        if st.markdown("<div style='height: 600px;'></div>", unsafe_allow_html=True):
            if st.session_state.right_clicked: # Only change if right is clicked
                st.session_state.right_clicked = False #reset
                if st.session_state.png_index < len(png_files) - 1:
                    st.session_state.png_index += 1
                    st.rerun()

    left_col, right_col = st.columns(2)
    if left_col.button("prev"):
        if st.session_state.png_index > 0:
                st.session_state.png_index -= 1
                st.rerun()
    if right_col.button("next"):
        if st.session_state.png_index < len(png_files) - 1:
                st.session_state.png_index += 1
                st.rerun()

if __name__ == "__main__":
    main()
