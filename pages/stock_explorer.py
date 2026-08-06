import streamlit as st
from components.page_title import render_page_title
from components.company_details import render_company_details
from components.kpis import render_kpis_one_row
from components.one_plot_container import render_one_plot_container
from components.historical_price_grid import render_historical_grid
from components.footer import render_footer
from components.spacer import spacer
from modules.kpis.company_data import (
    prepare_company_data,
    prepare_company_kpi_cards
)
from modules.charts.historical_price_chart import render_historical_price
from modules.grids.historical_grid_processing import prepare_historical_grid


company_dataframe = st.session_state.get("company_df")
stock_dataframe = st.session_state.get("stock_df")

if any(
    x is None
    for x in (
        company_dataframe,
        stock_dataframe,
    )
):
    st.warning(
        "Stock data or date range is unavailable. Please select a ticker first."
    )
    st.stop()

company_data = prepare_company_data(company_dataframe)


def render_stock_explorer():

    render_page_title("📊 Stock Explorer")

    render_company_details(company_data["company"])

    render_kpis_one_row(prepare_company_kpi_cards(company_data))

    spacer(2)

    render_one_plot_container(
        "Historical Price",
        render_historical_price(stock_dataframe)
    )

    spacer(2)

    render_historical_grid(
        prepare_historical_grid(stock_dataframe)
    )

    render_footer()



render_stock_explorer()