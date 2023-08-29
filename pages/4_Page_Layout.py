import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

from utils.utils import page_config

page_config(page_title='Layout')

st.title('Layout: Sidebar, Column, Tab, and Expander')

# side bar

space_slider = st.sidebar.slider(
    'Select Space Between the Two Charts', 0.0, 1.0, (0.5))


def plot_altair():
    st.markdown('')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    alt_chart = alt.Chart(chart_data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']).properties(
        title='Altair Chart')

    return alt_chart


def plot_vega():
    vega_chart = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "height": 300,
        "data": {
            "values": [
                {"category": "A", "group": "x", "value": 0.1},
                {"category": "A", "group": "y", "value": 0.6},
                {"category": "A", "group": "z", "value": 0.9},
                {"category": "B", "group": "x", "value": 0.7},
                {"category": "B", "group": "y", "value": 0.2},
                {"category": "B", "group": "z", "value": 1.1},
                {"category": "C", "group": "x", "value": 0.6},
                {"category": "C", "group": "y", "value": 0.1},
                {"category": "C", "group": "z", "value": 0.2}
            ]
        },
        "mark": "bar",
        "encoding": {
            "x": {"field": "category"},
            "y": {"field": "value", "type": "quantitative"},
            "xOffset": {"field": "group"},
            "color": {"field": "group"}
        },
        "title": "Vegar Bar Chart",
    }

    return vega_chart


def plot_plotly():
    df = px.data.gapminder()

    plotly_chart = px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
    )

    return plotly_chart


# column with buffer
col_left, _, col_right = st.columns([2, space_slider, 2])

with col_left:

    st.altair_chart(plot_altair(), theme=None, use_container_width=True)

with col_right:
    st.markdown('')
    st.vega_lite_chart(plot_vega(), theme=None, use_container_width=True)

# tab
alt_tab, vega_tab = st.tabs(['Altair Tab', 'Vega Tab'])

with alt_tab:
    st.altair_chart(plot_altair(), theme=None, use_container_width=True)

with vega_tab:
    st.vega_lite_chart(plot_vega(), theme=None, use_container_width=True)


# expander
with st.expander("See Plotly Chart"):
    st.plotly_chart(plot_plotly(), theme=None, use_container_width=True)
