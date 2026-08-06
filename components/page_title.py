import streamlit as st
from components.spacer import spacer


def render_page_title(title):
    st.title(title)

    spacer(1)