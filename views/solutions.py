import streamlit as st
import html
from data import SOLUTIONS, BU_NEEDS
from utils import stars, compute_score, score_label


def render():
    if st.session_state.get("selected_solution"):
        _render_detail(st.session_state.selected_solution)
    else:
        _render_list()


def _render_list():
    st.markdown("# Solutions Portfolio")
    st.markdown("<div style='color:#6b7280;font-size:14px;margin-bottom:20px;'>All benchmarked POCs and research proposals from the S&I team</div>", unsafe_allow_html=True)

    col_f1 = st.columns([1])[0]
    filter_type = col_f1.selectbox("Type", ["All", "POC", "Proposal"])

    filtered = [
        s for s in SOLUTIONS
        if (filter_type == "All" or s["type"] == filter_type)
        
    ]

    for s in filtered:
        tags_html = "".join(f"<span class='tag'>{html.escape(t)}</span>" for t in s["tags"])
        status_color = "#4ade80" if s["status"] == "Available" else "#fb923c"
        desc = html.escape(s["desc"])
        title = html.escape(s["title"])
        extra = ""
        if s["type"] == "Proposal":
            extra += f"<div style='margin-top:8px;font-size:12px;color:#6b7280;'>Difficulty: {stars(s.get('difficulty', 0))}</div>"
        card = (
            f"<div class='card'>"
            f"<div><span style='font-size:11px;color:#4b5563;'>{s['id']} · {s['type']}</span>"
            f"<div class='card-title'>{title}</div></div>"
            f"<span style='font-size:11px;font-weight:600;color:{status_color};'>&#9679; {s['status']}</span>"
            f"</div>"
            f"<div class='card-desc'>{desc}</div>"
            f"<div style='margin-top:10px;'>{tags_html}</div>"
            f"{extra}"
            f"</div>"
        )
        st.markdown(card, unsafe_allow_html=True)
        if st.button("View details →", key=f"sol_detail_{s['id']}"):
            st.session_state.selected_solution = s["id"]
            st.rerun()


def _render_detail(sol_id):
    sol = next((s for s in SOLUTIONS if s["id"] == sol_id), None)
    if sol is None:
        st.error("Solution not found.")
        return

    if st.button("← Back to Solutions"):
        st.session_state.selected_solution = None
        st.rerun()

    status_color = "#4ade80" if sol["status"] == "Available" else "#fb923c"
    tags_html = "".join(f"<span class='tag'>{html.escape(t)}</span>" for t in sol["tags"])

    st.markdown(f"""
    <div class="card" style="border-color:#4f8ef7;margin-bottom:24px;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div>
                <span style="font-size:11px;color:#4b5563;">{sol['id']} · {sol['type']}</span>
                <div class="card-title" style="font-size:20px;margin-top:4px;">{html.escape(sol['title'])}</div>
            </div>
            <span style="font-size:13px;font-weight:600;color:{status_color};">● {sol['status']}</span>
        </div>
    </div>""", unsafe_allow_html=True)

    col_left, col_right = st.columns([3, 1])

    with col_left:
        st.markdown("<div class='section-header'>Description</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='color:#d1d5db;font-size:14px;line-height:1.7;'>{html.escape(sol['desc'])}</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header' style='margin-top:20px;'>Tags</div>", unsafe_allow_html=True)
        st.markdown(f"<div>{tags_html}</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown("<div class='section-header'>Metadata</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card">
            <div style="font-size:12px;color:#6b7280;margin-bottom:4px;">Type</div>
                <div style="color:#d1d5db;font-size:13px;margin-bottom:12px;">{sol['type']}</div>
            <div style="font-size:12px;color:#6b7280;margin-bottom:4px;">Difficulty</div>
            <div style="font-size:13px;margin-bottom:12px;">{stars(sol.get('difficulty', 0))}</div>
            <div style="font-size:12px;color:#6b7280;margin-bottom:4px;">Status</div>
            <div style="color:{status_color};font-size:13px;">● {sol['status']}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div class='section-header' style='margin-top:28px;'>Matching Business Needs</div>", unsafe_allow_html=True)
    st.markdown("<div style='color:#6b7280;font-size:13px;margin-bottom:12px;'>BU needs ranked by keyword relevance to this solution</div>", unsafe_allow_html=True)

    scored_needs = sorted(
        [(n, compute_score(sol, n)) for n in BU_NEEDS],
        key=lambda x: -x[1]
    )

    for need, score in scored_needs:
        cls, label = score_label(score)
        pct = int(score * 100)
        urgency_color = {"High": "#f87171", "Medium": "#fb923c", "Low": "#a3a3a3"}[need["urgency"]]
        bar_color = "#4ade80" if cls == "high" else "#fb923c" if cls == "medium" else "#818cf8"
        st.markdown(f"""
        <div class="card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                <div>
                    <span style="font-size:11px;color:#4b5563;">{need['id']} · {need['unit']}</span>
                    <div class="card-title">{html.escape(need['title'])}</div>
                </div>
                <div style="text-align:right;">
                    <span class="match-badge {cls}">{label} · {pct}%</span><br>
                    <span style="font-size:11px;color:{urgency_color};margin-top:4px;display:block;">▲ {need['urgency']} urgency</span>
                </div>
            </div>
            <div class="card-desc">{html.escape(need['desc'])}</div>
            <div style="background:#0f1117;border-radius:4px;height:5px;margin:10px 0 4px 0;">
                <div style="background:{bar_color};height:5px;border-radius:4px;width:{pct}%;"></div>
            </div>
        </div>""", unsafe_allow_html=True)
        if st.button("View need details →", key=f"from_sol_{sol_id}_{need['id']}"):
            st.session_state.selected_solution = None
            st.session_state.selected_need = need["id"]
            st.session_state.current_view = "🏢 BU Needs"
            st.rerun()
