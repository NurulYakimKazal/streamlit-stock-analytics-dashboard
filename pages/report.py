import streamlit as st
import copy
from components.page_title import render_page_title
from components.company_details import render_company_details
from components.kpis import render_kpis_one_row
from components.kpis import render_kpis_two_rows
from components.one_plot_container import render_one_plot_container
from components.descriptive_statistics import render_descriptive_statistics
from components.footer import render_footer
from components.spacer import spacer
from modules.kpis.company_data import (
    prepare_company_data,
    prepare_company_kpi_cards
)
from modules.kpis.performance_overview import (
    prepare_performance_overview_data,
    prepare_performance_overview_kpi_cards
)
from modules.charts.cumulative_return_chart import render_cumulative_return
from modules.kpis.risk_analysis import (
    prepare_risk_analysis_data,
    prepare_risk_analysis_kpi_cards
)
from modules.charts.trend_indicators_chart import render_trend_indicators
from modules.grids.descriptive_statistics import prepare_descriptive_statistics_data
from modules.reports.pdf_report import generate_pdf_report


company_dataframe = st.session_state.get("company_df")
stock_dataframe = st.session_state.get("stock_df")

start_date = st.session_state.get("start_date")
end_date = st.session_state.get("end_date")

if any(
    x is None
    for x in (
        company_dataframe,
        stock_dataframe,
        start_date,
        end_date,
    )
):
    st.warning(
        "Stock data or date range is unavailable. Please select a ticker first."
    )
    st.stop()

company_data = prepare_company_data(company_dataframe)
performance_overview_data = prepare_performance_overview_data(stock_dataframe)
cumulative_return_figure = render_cumulative_return(stock_dataframe)
risk_analysis_data = prepare_risk_analysis_data(stock_dataframe)
trend_overview_figure = render_trend_indicators(stock_dataframe)
descriptive_statistics_data = prepare_descriptive_statistics_data(stock_dataframe)

pdf_bytes = generate_pdf_report(
    company_data,
    performance_overview_data,
    risk_analysis_data,
    descriptive_statistics_data,
    {
        "cumulative_return": copy.deepcopy(cumulative_return_figure),
        "trend": copy.deepcopy(trend_overview_figure),
    },
    start_date,
    end_date,
)

def render_report():

    render_page_title("📄 Stock Report")

    render_company_details(company_data["company"])

    st.markdown("### Market Snapshot")
    render_kpis_one_row(prepare_company_kpi_cards(company_data))

    spacer(2)

    st.markdown("### Performance Summary")
    render_kpis_two_rows(
        prepare_performance_overview_kpi_cards(performance_overview_data)
    )

    st.divider()
    spacer(1)

    render_one_plot_container(
        "Cumulative Return",
        cumulative_return_figure
    )

    st.divider()

    st.markdown("### Risk Summary")
    render_kpis_two_rows(
        prepare_risk_analysis_kpi_cards(risk_analysis_data)
    )

    st.divider()
    spacer(1)

    render_one_plot_container(
        "Trend Overview",
        trend_overview_figure
    )

    spacer(2)

    render_descriptive_statistics(
        descriptive_statistics_data
    )

    spacer(2)

    st.download_button(
        label="Download PDF Report",
        data=pdf_bytes,
        file_name=f"{company_data['company']['ticker']}_stock_report.pdf",
        mime="application/pdf",
    )

    render_footer()



render_report()