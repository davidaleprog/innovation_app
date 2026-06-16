import streamlit as st
from styles import inject_css
from views import overview, solutions, bu_needs, matching

st.set_page_config(
    page_title="Innovation Marketplace",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

NAV_OPTIONS = ["🏠 Overview", "🧪 Solutions Portfolio", "🏢 BU Needs", "🔗 Matching Engine"]

for key, default in [
    ("current_view", "🏠 Overview"),
    ("selected_solution", None),
    ("selected_need", None),
]:
    if key not in st.session_state:
        st.session_state[key] = default

with st.sidebar:
    st.markdown("## 🔬 Innovation Marketplace")
    st.markdown("<div style='color:#6b7280;font-size:13px;margin-bottom:20px;'>S&I internal platform — POC demo</div>", unsafe_allow_html=True)
    selected = st.radio(
        "Navigation",
        NAV_OPTIONS,
        index=NAV_OPTIONS.index(st.session_state.current_view),
        label_visibility="collapsed",
        key="nav_radio",
    )
    if selected != st.session_state.current_view:
        st.session_state.current_view = selected
        st.session_state.selected_solution = None
        st.session_state.selected_need = None
        st.rerun()
    st.markdown("---")
    st.markdown("<div style='color:#6b7280;font-size:11px;'>This demo uses keyword overlap as a proxy for semantic similarity. In production, a vector DB with sentence embeddings would power the matching.</div>", unsafe_allow_html=True)

view = st.session_state.current_view

if view == "🏠 Overview":
    overview.render()
elif view == "🧪 Solutions Portfolio":
    solutions.render()
elif view == "🏢 BU Needs":
    bu_needs.render()
elif view == "🔗 Matching Engine":
    matching.render()
