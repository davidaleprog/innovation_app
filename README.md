# 🔬 Innovation Marketplace

> **An asynchronous semantic matching platform connecting S&I innovations with business unit needs.**

A Streamlit-based demo showcasing how to systematically bridge the gap between innovation projects and business demand through intelligent matching and portfolio management.

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red) ![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Problem Statement

**The Challenge:** S&I teams generate innovative solutions, but timing often breaks the connection with business needs. How to:
- ✅ Keep innovation solutions discoverable and reusable?
- ✅ Capture business pain points in a structured way?
- ✅ Match them **asynchronously** at any time?
- ✅ Reduce time-to-impact while avoiding resource waste?

---

## 💡 Solution Overview

**The Innovation Marketplace** is an internal digital platform that:

1. **Exposes Innovation Solutions** — POCs and research proposals with benchmarked metrics, clear documentation, and reusable code
2. **Structures Business Needs** — BUs submit pain-point notes in a standardized format with keywords
3. **Matches Semantically** — powered by keyword overlap (demo) or vector embeddings (production)
4. **Tracks Adoption** — monitor which solutions get matched, adopted, or need re-exploration

### Key Workflow

```
SELECT → BENCHMARK → EXPOSE → LIST NEEDS → MATCH
  ↓         ↓          ↓          ↓         ↓
 Ideas    POC with   Portfolio  Pain     Semantic
          metrics    Package    Points   Search
```

---

## ✨ Features

### 📊 Overview Dashboard
- Real-time statistics (# solutions, # needs, # matches)
- Historical activity feed (recent benchmarks, registrations, new matches)
- Interactive workflow visualization

### 🧪 Solutions Portfolio
- **Browse** all POCs and research proposals with filters (Type, Domain)
- **Detail View** — full description, difficulty score, tags, metadata
- **Find Matches** — see which BU needs this solution can address (ranked by relevance)

### 🏢 Business Unit Needs
- **Register** pain-point notes from across the organization
- **Detail View** — problem context, urgency level, keywords
- **Discover Solutions** — ranked list of matching innovations

### 🔗 Matching Engine
- **Search Mode** — select a BU need → see all solutions ranked by relevance
- **Heatmap View** — full solution × need matrix with match scores
- **Cross-Navigation** — jump between solution and need detail pages seamlessly

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone repository
git clone https://github.com/davidaleprog/innovation_app.git
cd innovation_app

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`

---

## 📁 Project Structure

```
innovation_app/
├── app.py                      # Main Streamlit entry point
├── data.py                     # Solution & BU need data models
├── styles.py                   # Shared CSS styling (dark theme)
├── utils.py                    # Matching algorithms & helpers
├── views/
│   ├── __init__.py
│   ├── overview.py            # Dashboard & workflow intro
│   ├── solutions.py           # Portfolio list + detail view
│   ├── bu_needs.py            # BU needs list + detail view
│   └── matching.py            # Semantic search & heatmap
├── media/                      # Screenshots & assets
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🎨 UI Components

### **Solutions Portfolio View**
- Filterable card grid (by Type: POC/Proposal, Domain)
- Each card shows: title, description, tags, status badge
- **View Details →** button opens rich detail page with matching needs

### **BU Needs View**
- Structured pain-point cards with urgency indicators
- Keywords/tags for semantic matching
- **View Details →** reveals matched solutions ranked by relevance

### **Matching Engine**
- Two tabs:
  - 📍 **Find Solutions** — select a need, see ranked solutions with match % bars
  - 📋 **Heatmap** — full solution × need matrix, color-coded by match strength

### **Detail Pages**
- Unified layout: description on left, metadata sidebar on right
- **Cross-navigation** — click "View [solution/need] details →" to jump between pages
- Dynamic match scoring and visual indicators

---

## 🔧 How Matching Works

Currently uses **keyword overlap** as a matching proxy:

```python
score = |Solution.keywords ∩ Need.keywords| / min(|S|, |N|)
```

**Legend:**
- 🟢 **Strong (≥60%)** — high semantic similarity
- 🟡 **Partial (30–59%)** — moderate overlap
- 🔵 **Weak (<30%)** — limited relevance

**Production Plan:** Replace with vector embeddings (sentence transformers) + cosine similarity in a vector database for true semantic search.

---

## 📊 Data Models

### Solution
```python
{
    "id": "SOL-001",
    "title": "Anomaly Detection Framework",
    "type": "POC",  # or "Proposal"
    "domain": "Quality Control",
    "tags": ["time-series", "images", "unsupervised"],
    "difficulty": 3,
    "desc": "Full description...",
    "status": "Available",  # or "Proposed"
    "keywords": ["anomaly", "defect", "detection", ...]
}
```

### BU Need
```python
{
    "id": "BU-001",
    "unit": "Operations — Plant Lyon",
    "title": "Reduce false alarms on sensor lines",
    "desc": "Full problem statement...",
    "urgency": "High",  # or "Medium", "Low"
    "keywords": ["anomaly", "time series", "detection", ...]
}
```

---

## 🎓 Example Workflow

1. **Browse Solutions** → See "Anomaly Detection Framework" (POC, ⭐⭐⭐ difficulty)
2. **Click "View details"** → Read full description, see matching needs
3. **See Match** → "Reduce false alarms on sensor lines" (🟢 Strong 80% match)
4. **Click "View need details"** → Understand plant Lyon's pain point
5. **See Matched Solutions** → Confirm anomaly detection is ranked #1 for this need
6. **Take Action** → Connect operations team with S&I team

---

## 🛠️ Configuration & Extension

### Add New Solutions

Edit `data.py` → append to `SOLUTIONS`:

```python
{
    "id": "SOL-007",
    "title": "Your Innovation Title",
    "type": "POC",
    "domain": "Your Domain",
    "tags": ["tag1", "tag2"],
    "difficulty": 2,
    "desc": "Problem it solves...",
    "status": "Available",
    "keywords": ["keyword1", "keyword2", ...],
}
```

### Add New BU Needs

Edit `data.py` → append to `BU_NEEDS`:

```python
{
    "id": "BU-006",
    "unit": "Your Business Unit",
    "title": "Your Problem",
    "desc": "Detailed problem statement...",
    "urgency": "High",
    "keywords": ["keyword1", "keyword2", ...],
}
```

### Customize Styling

Edit `styles.py` to change colors, fonts, or component styling. Currently uses a professional dark theme with blue accents.

---

## 🚢 Deployment

### Option 1: Streamlit Cloud (Recommended) ⭐

1. Push repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository → Deploy
5. Get live URL: `https://your-app.streamlit.app`

### Option 2: Hugging Face Spaces

1. Create new Space with Streamlit runtime
2. Link to this GitHub repo
3. Auto-deploys on push

### Option 3: Docker + Cloud Run / Railway / Render

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

---

## 📈 Metrics & Success Measures

| Dimension | Proxy Metric |
|---|---|
| **Reusability** | % of solutions matched to ≥2 needs |
| **Adoption** | # of matched solution → implementation transitions |
| **Coverage** | % of high-urgency needs with strong matches |
| **Discovery** | # of cross-domain insights from matching |

---

## 🤝 Contributing

Contributions welcome! To add features:

1. Fork the repo
2. Create feature branch (`git checkout -b feature/my-feature`)
3. Commit changes (`git commit -m "Add my feature"`)
4. Push to branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📝 License

MIT License — see [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Alexis David** — Schneider Electric Innovation Team

- 🔗 [GitHub](https://github.com/davidaleprog)
- 💼 [LinkedIn](https://linkedin.com/in/alexis-david)

---

## 📖 Further Reading

- [Workflow & Architecture](docs/workflow.md) — detailed explanation of the 5-step process
- [Matching Algorithm](docs/matching.md) — semantic similarity scoring in production

---

**Questions or Feedback?** Open an issue or reach out!
