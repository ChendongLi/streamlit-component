import streamlit as st
from utils.utils import page_config
import pandas as pd

page_config(page_title='User Input')
st.title('User Input: Upload & Download')

# @st.cache_data(show_spinner='Loading...')
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv()


uploaded_file = st.file_uploader(label="Choose a CSV file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    if 'csv' in uploaded_file.name.split('.')[-1]:
        df_upload = pd.read_csv(uploaded_file)
        st.write(df_upload.head(50), use_container_width=True) 

        df_download = df_upload.to_csv(index=False)

        result = st.download_button(
            label="Download data as CSV",
            data=df_download ,
            file_name='iris.csv'
        )

        if result:
            st.write('Complete Downloading')

    else:
        st.write('Please upload csv format data file')