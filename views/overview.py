import streamlit as st
from data import SOLUTIONS, BU_NEEDS


def render():
    st.markdown("# Innovation Marketplace")
    st.markdown("<div style='color:#6b7280;font-size:15px;margin-bottom:28px;'>Asynchronously connecting S&I innovation with Business Unit needs</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, num, label in [
        (c1, len(SOLUTIONS), "Solutions available"),
        (c2, sum(1 for s in SOLUTIONS if s["type"] == "POC"), "POCs benchmarked"),
        (c3, len(BU_NEEDS), "BU needs registered"),
        (c4, sum(1 for n in BU_NEEDS if n["urgency"] == "High"), "High-urgency needs"),
    ]:
        col.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{num}</div>
            <div class="stat-label">{label}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
   