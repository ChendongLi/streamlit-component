import streamlit as st
from PIL import Image 

def page_config(page_title: str, 
                favicon_path: str='assets/streamlit_favicon.png'):
    icon_img = Image.open(favicon_path)

    st.set_page_config(page_title = page_title, 
                       page_icon = icon_img, 
                       layout='wide')
    
    move_title_up = '<style>div.block-container{padding-top:1rem;}</style>'
    st.markdown(move_title_up, unsafe_allow_html=True)

    hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
    st.markdown(hide_default_format, unsafe_allow_html=True)