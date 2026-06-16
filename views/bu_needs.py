import streamlit as st
import html
from data import BU_NEEDS, SOLUTIONS
from utils import compute_score, score_label


def render():
    if st.session_state.get("selected_need"):
        _render_detail(st.session_state.selected_need)
    else:
        _render_list()


def _render_list():
    st.markdown("# Business Unit Needs")
    st.markdown("<div style='color:#6b7280;font-size:14px;margin-bottom:20px;'>Structured pain-point notes submitted by BUs</div>", unsafe_allow_html=True)

    for n in BU_NEEDS:
        urgency_color = {"High": "#f87171", "Medium": "#fb923c", "Low": "#a3a3a3"}[n["urgency"]]
        kw_html = "".join(f"<span class='tag'>{html.escape(k)}</span>" for k in n["keywords"])
        st.markdown(f"""
        <div class="card">
            <div style="display:flex;justify-content:space-between;">
                <span style="font-size:11px;color:#4b5563;">{n['id']} · {n['unit']}</span>
                <span style="font-size:11px;font-weight:600;color:{urgency_color};">▲ {n['urgency']} urgency</span>
            </div>
            <div class="card-title">{html.escape(n['title'])}</div>
            <div class="card-desc">{html.escape(n['desc'])}</div>
            <div style="margin-top:10px;">{kw_html}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("View details →", key=f"need_detail_{n['id']}"):
            st.session_state.selected_need = n["id"]
            st.rerun()

    st.markdown("---")
    st.markdown("### Submit a new need")
    with st.expander("➕ Register a BU pain point"):
        bu_name = st.text_input("Business Unit")
        need_title = st.text_input("Need title")
        need_desc = st.text_area("Description (1-page note)", height=120)
        urgency = st.select_slider("Urgency", ["Low", "Medium", "High"])
        if st.button("Submit need"):
            st.success("✅ Need registered and queued for semantic indexing.")


def _render_detail(need_id):
    need = next((n for n in BU_NEEDS if n["id"] == need_id), None)
    if need is None:
        st.error("Need not found.")
        return

    if st.button("← Back to BU Needs"):
        st.session_state.selected_need = None
        st.rerun()

    urgency_color = {"High": "#f87171", "Medium": "#fb923c", "Low": "#a3a3a3"}[need["urgency"]]
    kw_html = "".join(f"<span class='tag'>{html.escape(k)}</span>" for k in need["keywords"])

    st.markdown(f"""
    <div class="card" style="border-color:#4f8ef7;margin-bottom:24px;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div>
                <span style="font-size:11px;color:#4b5563;">{need['id']} · {need['unit']}</span>
                <div class="card-title" style="font-size:20px;margin-top:4px;">{html.escape(need['title'])}</div>
            </div>
            <span style="font-size:13px;font-weight:600;color:{urgency_color};">▲ {need['urgency']} urgency</span>
        </div>
    </div>""", unsafe_allow_html=True)

    col_left, col_right = st.columns([3, 1])

    with col_left:
        st.markdown("<div class='section-header'>Description</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='color:#d1d5db;font-size:14px;line-height:1.7;'>{html.escape(need['desc'])}</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header' style='margin-top:20px;'>Keywords</div>", unsafe_allow_html=True)
        st.markdown(f"<div>{kw_html}</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown("<div class='section-header'>Metadata</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card">
            <div style="font-size:12px;color:#6b7280;margin-bottom:4px;">Business Unit</div>
            <div style="color:#d1d5db;font-size:13px;margin-bottom:12px;">{html.escape(need['unit'])}</div>
            <div style="font-size:12px;color:#6b7280;margin-bottom:4px;">Urgency</div>
            <div style="color:{urgency_color};font-size:13px;">▲ {need['urgency']}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div class='section-header' style='margin-top:28px;'>Matching Solutions</div>", unsafe_allow_html=True)
    st.markdown("<div style='color:#6b7280;font-size:13px;margin-bottom:12px;'>Solutions ranked by keyword relevance to this need</div>", unsafe_allow_html=True)

    scored_solutions = sorted(
        [(s, compute_score(s, need)) for s in SOLUTIONS],
        key=lambda x: -x[1]
    )

    for sol, score in scored_solutions:
        cls, label = score_label(score)
        pct = int(score * 100)
        status_color = "#4ade80" if sol["status"] == "Available" else "#fb923c"
        bar_color = "#4ade80" if cls == "high" else "#fb923c" if cls == "medium" else "#818cf8"
        tags_html = "".join(f"<span class='tag'>{html.escape(t)}</span>" for t in sol["tags"])
        st.markdown(f"""
        <div class="card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                <div>
                    <span style="font-size:11px;color:#4b5563;">{sol['id']} · {sol['type']}</span>
                    <div class="card-title">{html.escape(sol['title'])}</div>
                </div>
                <div style="text-align:right;">
                    <span class="match-badge {cls}">{label} · {pct}%</span><br>
                    <span style="font-size:11px;color:{status_color};margin-top:4px;display:block;">● {sol['status']}</span>
                </div>
            </div>
            <div class="card-desc">{html.escape(sol['desc'])}</div>
            <div style="background:#0f1117;border-radius:4px;height:5px;margin:10px 0 6px 0;">
                <div style="background:{bar_color};height:5px;border-radius:4px;width:{pct}%;"></div>
            </div>
            <div style="margin-top:4px;">{tags_html}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("View solution details →", key=f"from_need_{need_id}_{sol['id']}"):
            st.session_state.selected_need = None
            st.session_state.selected_solution = sol["id"]
            st.session_state.current_view = "🧪 Solutions Portfolio"
            st.rerun()
