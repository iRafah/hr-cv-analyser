# 📄 HR CV Analyser

HR CV Analyser is a Streamlit-based application that uses the OpenAI GPT API to analyze a candidate's CV against a job description. It identifies missing skills, provides a compatibility score, and offers reasoning about the match — helping recruiters and applicants better understand CV relevance.

---

## 🔍 Features

- Upload your **CV** (PDF - for now)
- Paste a **Job Description**
- Uses **ChatGPT** (OpenAI API) for:
  - Semantic analysis
  - Match scoring (e.g., 78% compatible)
  - Skill gap detection
  - Context-aware reasoning
- Outputs are neatly formatted using Streamlit

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API Key
- Required packages (see below)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cv-analyst.git
   cd cv-analyst
2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # or .\venv\Scripts\activate on Windows
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
4. **Set your OpenAI API Key:**

    **Create a .streamlit/secrets.toml file:**
    ```bash
    [openai]
    OPENAI_API_KEY = "your_openai_api_key_here"
5. **Run the app:**
    ```bash
    streamlit run app.py

## 📌 Example Output
🚀 Match Score: 84%

🚀 Missing Skills: ['docker', 'unit testing', 'graphql']

🚀 Reasoning: The candidate demonstrates strong alignment with backend technologies mentioned in the JD, but lacks DevOps tools and testing experience...
