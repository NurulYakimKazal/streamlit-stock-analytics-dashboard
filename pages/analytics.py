import streamlit as st
from components.page_title import render_page_title
from components.company_details import render_company_details
from components.kpis import render_kpis_two_rows
from components.one_plot_container import render_one_plot_container
from components.chart_grid_container import render_chart_grid_container
from components.descriptive_statistics import render_descriptive_statistics
from components.footer import render_footer
from components.spacer import spacer
from modules.kpis.company_data import prepare_company_data
from modules.kpis.performance_overview import (
    prepare_performance_overview_data,
    prepare_performance_overview_kpi_cards
)
from modules.charts.cumulative_return_chart import render_cumulative_return
from modules.charts.return_analysis_charts import (
    render_daily_returns,
    render_return_histogram
)
from modules.kpis.risk_analysis import (
    prepare_risk_analysis_data,
    prepare_risk_analysis_kpi_cards
)
from modules.charts.trend_indicators_chart import render_trend_indicators
from modules.charts.volume_activity_chart import render_volume_activity
from modules.grids.descriptive_statistics import prepare_descriptive_statistics_data


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
performance_overview_data = prepare_performance_overview_data(stock_dataframe)
risk_analysis_data = prepare_risk_analysis_data(stock_dataframe)


def render_analytics():

    render_page_title("📈 Analytics")

    render_company_details(company_data["company"])

    st.markdown("### Performance Overview")
    render_kpis_two_rows(
        prepare_performance_overview_kpi_cards(performance_overview_data)
    )

    st.divider()
    spacer(1)

    render_one_plot_container(
        "Cumulative Return",
        render_cumulative_return(stock_dataframe)
    )

    spacer(2)

    render_chart_grid_container(
        [
            ("Daily Return", render_daily_returns(stock_dataframe)),
            ("Return Histogram", render_return_histogram(stock_dataframe)),
        ]
    )

    st.divider()

    st.markdown("### Risk Analysis")
    render_kpis_two_rows(
        prepare_risk_analysis_kpi_cards(risk_analysis_data)
    )

    st.divider()
    spacer(1)

    render_one_plot_container(
        "Trend Indicators",
        render_trend_indicators(stock_dataframe)
    )

    spacer(2)

    render_one_plot_container(
        "Volume Activity",
        render_volume_activity(stock_dataframe)
    )

    spacer(2)

    render_descriptive_statistics(
        prepare_descriptive_statistics_data(stock_dataframe)
    )

    render_footer()



render_analytics()