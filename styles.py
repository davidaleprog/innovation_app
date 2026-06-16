import streamlit as st


def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Space+Grotesk:wght@500;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Page background */
.stApp { background-color: #0f1117; }

h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; }

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #16191f !important;
    border-right: 1px solid #2a2d35;
}

/* Cards */
.card {
    background: #16191f;
    border: 1px solid #2a2d35;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 14px;
    transition: border-color 0.2s;
}
.card:hover { border-color: #4f8ef7; }

.card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 6px;
}
.card-meta {
    font-size: 12px;
    color: #ffffff;
    margin-bottom: 8px;
}
.card-desc {
    font-size: 13px;
    color: #ffffff;
    line-height: 1.55;
}

/* Match badge */
.match-badge {
    display: inline-block;
    background: linear-gradient(135deg, #1a3a5c, #1e4d7b);
    border: 1px solid #4f8ef7;
    color: #7eb3f7;
    font-size: 11px;
    font-weight: 600;
    border-radius: 20px;
    padding: 3px 10px;
    margin-top: 10px;
}
.match-badge.high   { background: linear-gradient(135deg, #14532d, #166534); border-color: #4ade80; color: #86efac; }
.match-badge.medium { background: linear-gradient(135deg, #422006, #7c2d12); border-color: #fb923c; color: #fdba74; }
.match-badge.low    { background: linear-gradient(135deg, #312e81, #3730a3); border-color: #818cf8; color: #a5b4fc; }

/* Tags */
.tag {
    display: inline-block;
    background: #1e2330;
    color: #ffffff;
    font-size: 11px;
    border-radius: 4px;
    padding: 2px 8px;
    margin: 2px 3px 2px 0;
    border: 1px solid #2a2d35;
}

/* Section headers */
.section-header {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #4f8ef7;
    margin: 18px 0 10px 0;
}

/* Stat boxes */
.stat-box {
    background: #16191f;
    border: 1px solid #2a2d35;
    border-radius: 8px;
    padding: 14px 16px;
    text-align: center;
}
.stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #4f8ef7;
}
.stat-label {
    font-size: 11px;
    color: #ffffff;
    margin-top: 2px;
}

/* Divider */
hr { border-color: #2a2d35; }

/* Match connector line */
.connector {
    text-align: center;
    font-size: 22px;
    color: #4f8ef7;
    padding: 6px 0;
}
</style>
""", unsafe_allow_html=True)
