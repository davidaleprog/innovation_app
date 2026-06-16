# 🔬 Innovation Marketplace

> **An asynchronous semantic matching platform connecting innovation solutions with business unit needs.**

A Streamlit-based demonstration of a systematic workflow to bridge the gap between S&I innovation projects and business demand, reducing time-to-impact while ensuring solutions are discoverable, reusable, and impactful.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/<your-username>/<your-repo>/main) [![Run in Docker](https://img.shields.io/badge/Docker-Run-blue)](https://hub.docker.com/)

---

## 🎯 The Challenge

Innovation teams generate valuable knowledge, methods, and ideas—but these intangible assets have no physical "place to live" except in our brains. This creates a timing bottleneck:

1. **S&I Team** needs to keep **up to date** about AI opportunities
2. S&I has to **bring impact to business units** without "running behind"
3. Need to **benchmark** and demonstrate efficiency of innovation projects
4. Need **reusable and evolution-ready solutions**
5. Need better **exposition of innovative works**
6. Need **comprehension of business unit (BU) needs**
7. **Timing mismatch** — solution offer and business demand are misaligned
8. **Speed** — accelerate time-to-impact

### The Root Problem

When innovation is discovered, documented, and evaluated in isolation, it cannot connect with emerging business needs at the right moment. Conversely, when business needs are articulated, no systematic way exists to search for relevant past work across the organization.

---

## 💡 The Solution: An Internal Innovation Marketplace

**Core Idea:** Create a **digital "marketplace"** where innovation solutions meet business demand asynchronously—decoupling creation time from adoption time.

Instead of waiting for perfect timing between project completion and business readiness, this platform allows:
- ✅ Solutions to live and be discoverable in a centralized portfolio
- ✅ Business needs to be formulated, stored, and searched at any time
- ✅ Semantic matching to surface relevant connections automatically
- ✅ Reusability across projects and teams

---

## 🔄 The Five-Step Workflow

<img src="media/innovation_schema.excalidraw.png" width="800" alt="Innovation Schema">

### 1️⃣ **Selection**

To stay ahead of innovation and avoid running behind business needs, S&I must continuously explore emerging trends, literature, and competitor innovations. This first step constist in extracting pormising research directions among this amount of information.

**Activities:**
- Automated literature review (coordinated effort, shared tools)
- Competitive intelligence gathering
- Identification of exploratory projects with potential value

---

### 2️⃣ **Benchmarking**

This stage concerns launched research projects. Any research work's value is legitimized through comparison against **standardized datasets with well-defined metrics**.

**Approach:**
- Develop **POCs**  that demonstrate added value without targeting full industrialization (limited time invested)
- Use **standard benchmark datasets** across the organization
- Document reproducible results and metrics
- Avoid wasting development time on projects without validated RIO

**Outcomes:** Benchmarked POC with clear metrics showing relative performance

---

### 3️⃣ **Expose Solutions**

Solutions are packaged and exposed in two formats:

#### **POC (Proof of Concept)**
- Result of short exploratory work leading to benchmarked results
- Not yet ready to industrialize
- **Duration:** Few months maximum
- **Goal:** Demonstrate feasibility and impact quickly

**Reusability Challenge:** Look for redundancies across research projects. For example:
- If work exists on anomaly detection for *images* and separately for *time series*, create a general Python package applicable to both
- Abstract methods beyond their original problem context
- Build solutions that work *independent of input type and domain specificity*
- Shift toward *problem agnostic* solutions

#### **Proposal (Research Direction)**
- Well-documented potential research directions
- Exposed to entire organization for impact assessment and feasibility review
- Helps pool resources and mitigate risks
- BUs can "vote" for proposals to support launch decisions

#### **Exposure Formats** (by priority)

1. **1-Page Keynote** — high-level summary with general taxonomy
2. **Contact List** — key stakeholders for dialogue
3. **Reproducible Code** — fully documented and executable
4. **5-Minute Video** — quick overview for busy stakeholders

**Digital Storage:** Solutions are catalogued in a **vector database** enabling semantic search and information retrieval across unstructured documentation.

---

### 4️⃣ **List Pain Points**

After an exhaustive inventory of business pain points, stakeholders (PMs, domain experts, or anyone in S&I) write keynotes describing their needs precisely.

**Process:**
- Document pain point in concrete business language
- Optionally rewrite using **LLMs** into more abstract, generic language facilitating matching with solution syntaxe
- **Note:** S&I members can also register internal needs (e.g., "I need a benchmark for anomaly detection with standard metrics"), allowing cross-team reuse

**Key Insight:** A well-formulated internal pain point from one team may avoid repetitive work for other BUs.

---

### 5️⃣ **Matching**

With precise solution descriptions and refined business need formulations, an **asynchronous "marketplace"** emerges where supply and demand meet at any time.

**Matching Mechanism:**
- Semantic search powered by keyword overlap (demo) or vector embeddings (futurn versions)
- Multiple discovery modes:
  - Search for solutions matching a specific business need
  - Browse solutions and see which needs they address
  - View full solution × need correlation matrix
- **Result:** Ranked matches with relevance scores

---

## ✨ Key Characteristics of This Workflow

### 🎯 **Measurable Success**

Track organizational learning and impact:

| Metric | Definition | Use Case |
|--------|-----------|----------|
| **Reusability %** | % of innovation projects reused across teams | Assess packaging quality and abstraction |
| **Adoption %** | % of exposed solutions matched with needs | Gauge portfolio quality |
| **Unmatchable %** | % of solutions with no matches | Extract patterns → inform future exploration |
| **Time-to-Match** | Days between solution exposure and first match | Measure marketplace velocity |

### 🏆 **Support Project Ranking**

Systematically answer questions for prioritization:
- **What is the best match?** → Closest innovation to business need (highest relevance score)
- **Easiest to industrialize?** → Consider complexity score and resource requirements
- **Most impactful?** → Combine adoption score, business need urgency, and strategic alignment
- **Most resource-hungry?** → Filter by estimated development effort

### 🤝 **Bridge Business-S&I Dialogue**

- **From S&I perspective:** Satisfying to expose work to anyone spending time on the innovation marketplace
- **From BU perspective:** Simple 1-page need description (no lengthy meetings, no lexical friction)
- **Interface:** Dedicated persons or LLMs mediate between domains

---

## Installation

Run the app locally or deploy it to Streamlit Cloud. Quick instructions below — copy & paste.

Run locally
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Streamlit Cloud (easy deploy)

1. Push this repository to GitHub.
2. Go to https://share.streamlit.io and connect your GitHub account.
3. Select this repository and the branch (e.g. `main`) to deploy.
4. Use the live URL shown by Streamlit Cloud. Replace the Streamlit badge link above with the live URL when available.

Optional: Docker

Create a `Dockerfile` (example below) and build the image to run anywhere.

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t innovation_app .
# Run the container, mapping the container port 8501 to the host
docker run --rm -p 8501:8501 innovation_app

# If you want to mount the code (for live edits) and use the host Python
# (useful for development), run the app locally instead of inside Docker.

Open http://localhost:8501 in your browser after the container starts.
```

Optional: Hugging Face Spaces

1. Create a new Space with the Streamlit runtime.
2. Link the GitHub repository and deploy. Use the badge above if you publish there.

Try it (placeholder)

Once deployed, add a direct `Try it` link near the top of this README pointing to the Streamlit URL so visitors can open the app in one click.