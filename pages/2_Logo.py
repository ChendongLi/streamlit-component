import base64
import streamlit as st


@st.cache_resource()
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="10% 10%",
    margin_top="5%",
    margin_left="0%",
    image_width="20%",
    image_height="20%",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stAppViewContainer"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    margin-left: %s ;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        margin_left,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )


add_logo('assets/streamlit_logo.png')