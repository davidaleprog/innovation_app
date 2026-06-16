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
    st.image("media/innovation_schema.excalidraw.png", use_container_width=True)

    with st.expander("📋 About this project — context & proposed workflow", expanded=True):
        st.markdown("""
## Introduction

Among all the issues pointed out, a recurrent topic was: **How to bring impact to business with innovative solutions?**

The numerous topics tackled during the workshop made me try to think about how to match innovation solutions and business needs in a settings where both sides evolve quickly. In particular, it appeared to be necessary to imagine how to perform such matching in an **asynchronous** way.

---

### Challenges

1. S&I team has the responsibility to keep **up to date** about AI opportunities
2. S&I team has to **bring impact to business units** without "running behind"
3. Need to **benchmark** and demonstrate efficiency of innovation projects
4. Would benefit from making **reusable and evolution-ready solutions**
5. Need better **exposition of innovative works**
6. Need better dialogue and **comprehension of business unit (BU) needs**
7. Find good **timing** between solution offer and business demand
8. **Speed**: accelerate time-to-impact

### Ideas
- Create benchmarks and standard datasets for demonstrating solution efficiency
- Write clear notes of what has been done during an innovation project
- Build a pool of past innovation projects
- Standardise research direction proposals

---

## Proposed Workflow

The core idea is creating an **Innovation Portfolio linked to an internal business search engine** — in short, an internal digital *marketplace* where innovation solutions can meet business demand to circumvent the timing bottleneck.

S&I's job is to produce knowledge, methods and ideas. Since this is not material, this knowledge has no place to live except in our brains, making it difficult to turn ideas into reality. The goal is to constitute a digital place where future and former ideas can live and find connections with business — leveraging language models, embedding techniques, and vector search.

### 1 · Selection
Stay ahead of innovation by continuously exploring literature and competitor advances. Select exploratory projects with potential value. Automated literature review agents and shared centralised tooling can lower the access effort.

### 2 · Benchmarking
Whatever the research work, its value is legitimated by comparison to baselines on a **standardised dataset with well-defined metrics**. The idea: demonstrate added value with a POC that doesn't target industrialisation (yet), avoiding unnecessary development waste without ROI guaranty.

### 3 · Expose Solutions

Solutions can be of two types:
- **POC** — result of short exploratory work leading to benchmarked results, not production-ready yet. Should not exceed a few months.
- **Proposal** — well-documented potential research directions exposed to everyone to assess ROI and feasibility.

**Format** *(by priority)*: 1-page keynote · list of contacts · reproducible code · accessible demo · 5-min video

For POCs: find redundancies across projects and combine them into **generalised, reusable solutions** (e.g. a single anomaly detection package working on both images and time series). Store keynotes in a vector database for semantic search at the matching step.

For Proposals, include: expected outcomes · difficulty score · resources · expected development time. BUs can "vote" for proposals that would bring most impact — supporting project launch decisions.

### 4 · List Pain Points
After exhaustive listing of business pain points, any relevant person writes a keynote describing their need precisely. An optional LLM-assisted rewrite can generalise the note to improve matching with available solutions.

This also works *within* S&I: a member needing a forecasting architecture can find it if a colleague worked on it — avoiding repetitive tasks.

### 5 · Matching
With precise solution descriptions on one side and refined business need formulations on the other, the **asynchronous marketplace** lets offer and demand meet at any time — powered by semantic similarity (vector embeddings + cosine distance in production).

---

## Interesting Characteristics

| Dimension | Metric |
|---|---|
| Reusability | % of reusable projects |
| Adoption | % of unmatched solutions → patterns → future exploration decisions |
| Success history | Patterns in historical matching successes & failures |

**Project ranking support** — answers questions such as: What is the closest innovation to a business need? The easiest to industrialise? The most impactful? The most resource-intensive?
        """)

    st.markdown("### How it works")

    cols = st.columns(5)
    steps = [
        ("1", "Select", "Explore literature & competitors. Pick exploratory projects."),
        ("2", "Benchmark", "Build POC with standardised datasets & clear metrics."),
        ("3", "Expose", "Publish keynote + package into searchable portfolio."),
        ("4", "List needs", "BUs describe pain points as structured 1-page notes."),
        ("5", "Match", "Semantic search links solutions to needs — asynchronously."),
    ]
    for col, (num, title, desc) in zip(cols, steps):
        col.markdown(f"""
        <div class="card" style="text-align:center;">
            <div style="font-size:24px;font-family:'Space Grotesk',sans-serif;color:#4f8ef7;font-weight:700;">{num}</div>
            <div class="card-title" style="text-align:center;">{title}</div>
            <div class="card-desc">{desc}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Innovation schema")

    st.markdown("---")
    st.markdown("### Recent activity")
    activity = [
        ("🧪", "SOL-005", "Visual Inspection Co-pilot benchmarked on Bordeaux pilot line", "2 days ago"),
        ("🏢", "BU-004", "Legal — Procurement registered new need: contract review", "3 days ago"),
        ("🔗", "", "New strong match found: SOL-003 ↔ BU-003 (supply chain)", "5 days ago"),
        ("🧪", "SOL-006", "Customer Churn Predictor POC published", "1 week ago"),
    ]
    for icon, tag, text, when in activity:
        st.markdown(f"""
        <div style="display:flex;align-items:flex-start;gap:12px;padding:10px 0;border-bottom:1px solid #2a2d35;">
            <span style="font-size:18px;">{icon}</span>
            <div>
                {"<span class='tag'>"+tag+"</span> " if tag else ""}
                <span style="color:#d1d5db;font-size:13px;">{text}</span><br>
                <span style="color:#4b5563;font-size:11px;">{when}</span>
            </div>
        </div>""", unsafe_allow_html=True)
