import streamlit as st
from utils.utils import page_config
import pandas as pd

page_config(page_title='Session State')
st.title('Add Statefulness: Session State & Callback')

# *************** stateless ****************************
st.markdown('### Stateless Example: Counter')
count = 0

increment = st.button('Statelss Increment')
if increment:
    count += 1

st.write('Count = ', count)

st.markdown('')


# *************** stateful ****************************

st.markdown('### *Stateful* Example: Counter')

if 'count' not in st.session_state:
    st.session_state['count'] = 0

increment = st.button('Stateful Increment')
if increment:
    st.session_state['count'] += 1

st.write('Count = ', st.session_state['count'])

st.markdown('')


# *************** call back ****************************

st.markdown('### CallBack Function')
st.write("st.session_state object:", st.session_state)


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2406


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2406


col1, _, col2 = st.columns([2, 0.5, 2])
with col1:
    pounds = st.number_input('Pounds:', key='lbs', on_change=lbs_to_kg)

with col2:
    kgs = st.number_input('Kilograms:', key='kg', on_change=kg_to_lbs)
