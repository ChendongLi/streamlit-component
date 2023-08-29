import base64
import streamlit as st
from PIL import Image
from utils.utils import page_config

page_config(page_title='Logo')

# add logo on top of page title

img = Image.open('assets/cisco_logo.png')
new_img = img.resize((120, 60))
st.image(new_img)

st.title('Add Logo to the Page')


# add logo on top of sidebar

@st.cache_resource()
def get_base64_image(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_css_for_logo(
    png_file,
    background_position="10% 5%",
    image_width="40%",
    image_height="30%",
):
    binary_string = get_base64_image(png_file)
    return f"""
            <style>
                [data-testid="stSidebarNav"] {{
                    background-image: url("data:image/png;base64,{binary_string}");
                    background-repeat: no-repeat;
                    background-position: {background_position};
                    background-size: {image_width}, {image_height};
                }}
            </style>
            """


def add_logo(png_file):
    logo_css = build_css_for_logo(png_file)
    st.markdown(
        logo_css,
        unsafe_allow_html=True,
    )


add_logo('assets/cisco_logo.png')
