import streamlit as st
import pandas as pd
from data import SOLUTIONS, BU_NEEDS
from utils import compute_score, score_label


def render():
    st.markdown("# Matching Engine")
    st.markdown("<div style='color:#6b7280;font-size:14px;margin-bottom:20px;'>Asynchronous marketplace — solutions meet business needs</div>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔍 Find solutions for a need", "📋 All matches heatmap"])

    with tab1:
        need_titles = {n["title"]: n for n in BU_NEEDS}
        selected_title = st.selectbox("Select a BU need", list(need_titles.keys()))
        need = need_titles[selected_title]

        st.markdown(f"""
        <div class="card" style="border-color:#4f8ef7;">
            <div style="font-size:11px;color:#4b5563;">{need['id']} · {need['unit']}</div>
            <div class="card-title">{need['title']}</div>
            <div class="card-desc">{need['desc']}</div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<div class='section-header'>Matching solutions — ranked by relevance</div>", unsafe_allow_html=True)

        scored = sorted(
            [(s, compute_score(s, need)) for s in SOLUTIONS],
            key=lambda x: -x[1]
        )

        for sol, score in scored:
            cls, label = score_label(score)
            pct = int(score * 100)
            tags_html = "".join(f"<span class='tag'>{t}</span>" for t in sol["tags"])
            status_color = "#4ade80" if sol["status"] == "Available" else "#fb923c"
            bar_color = "#4ade80" if cls == "high" else "#fb923c" if cls == "medium" else "#818cf8"
            st.markdown(f"""
            <div class="card">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div>
                        <span style="font-size:11px;color:#4b5563;">{sol['id']} · {sol['type']}</span>
                        <div class="card-title">{sol['title']}</div>
                    </div>
                    <div style="text-align:right;">
                        <span class="match-badge {cls}">{label} · {pct}%</span><br>
                        <span style="font-size:11px;color:{status_color};margin-top:4px;display:block;">● {sol['status']}</span>
                    </div>
                </div>
                <div class="card-desc">{sol['desc']}</div>
                <div style="background:#0f1117;border-radius:4px;height:5px;margin:10px 0 6px 0;">
                    <div style="background:{bar_color};height:5px;border-radius:4px;width:{pct}%;"></div>
                </div>
                <div style="margin-top:4px;">{tags_html}</div>
            </div>""", unsafe_allow_html=True)

    with tab2:
        st.markdown("**Match score matrix** — keyword overlap score (proxy for semantic similarity)")

        data = {}
        for need in BU_NEEDS:
            row = {}
            for sol in SOLUTIONS:
                row[sol["id"]] = int(compute_score(sol, need) * 100)
            data[need["id"]] = row

        df = pd.DataFrame(data).T
        df.index = [n["id"] for n in BU_NEEDS]
        df.columns = [s["id"] for s in SOLUTIONS]

        def color_cell(val):
            if val >= 60:
                return "background-color:#14532d;color:#86efac"
            elif val >= 30:
                return "background-color:#422006;color:#fdba74"
            else:
                return "background-color:#1e1e2e;color:#4b5563"

        styled = df.style.applymap(color_cell).format("{}%")
        st.dataframe(styled, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Legend:** <span style='color:#86efac'>■ Strong (≥60%)</span> &nbsp; <span style='color:#fdba74'>■ Partial (30–59%)</span> &nbsp; <span style='color:#4b5563'>■ Weak (<30%)</span>", unsafe_allow_html=True)
        st.markdown("<div style='color:#4b5563;font-size:12px;margin-top:8px;'>In production, scores would come from cosine similarity between sentence embeddings stored in a vector database.</div>", unsafe_allow_html=True)
