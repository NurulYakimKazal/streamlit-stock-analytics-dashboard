import streamlit as st
from modules.utils.no_data_warning import show_no_stock_data_warning


def render_descriptive_statistics(df):
    with st.expander("Descriptive Statistics", expanded=True):

        if df.empty:
            show_no_stock_data_warning()
        else:
            st.dataframe(
                df,
                width="stretch",
                hide_index=True,
            )