import streamlit as st
from modules.utils.no_data_warning import show_no_stock_data_warning


def render_historical_grid(stock_df):
    with st.expander("Historical Price Data"):
        if stock_df.empty:
            show_no_stock_data_warning()
        else:
            st.dataframe(
                stock_df,
                column_config={
                    "Open": st.column_config.NumberColumn(format="%.2f"),
                    "High": st.column_config.NumberColumn(format="%.2f"),
                    "Low": st.column_config.NumberColumn(format="%.2f"),
                    "Close": st.column_config.NumberColumn(format="%.2f"),
                },
                width='stretch',
                hide_index=True,
            )