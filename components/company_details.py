import streamlit as st
from components.spacer import spacer


def render_company_details(company):

    st.header(f"{company['name']} ({company['ticker']})")
    st.caption(f"{company['sector']} • {company['industry']}")

    spacer(2)