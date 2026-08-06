import streamlit as st

def render_kpis_one_row(kpis):
    cols = st.columns(len(kpis), gap="xsmall", border=True)

    for col, (label, value) in zip(cols, kpis.items()):
        with col:
            st.metric(label, value)


def render_kpis_two_rows(kpis):
    items = list(kpis.items())
    mid = (len(items) + 1) // 2  # First row gets the extra item if odd

    rows = [items[:mid], items[mid:]]

    for row in rows:
        cols = st.columns(len(row), gap="xsmall", border=True)
        for col, (label, value) in zip(cols, row):
            with col:
                st.metric(label, value)