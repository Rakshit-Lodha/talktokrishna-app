# 🕉️ Talk to Krishna

An AI-powered spiritual counselor that provides guidance from the Bhagavad Gita for modern life problems. Built to help people navigate heartbreak, career stress, and life's challenges through ancient wisdom.

**🔗 [Try it live](https://talktokrishna-app.streamlit.app/)**
<img width="860" height="646" alt="image" src="https://github.com/user-attachments/assets/b7a3c50b-a24d-4f76-b12d-2f64e28c1684" />


## ✨ What It Does

Ask Krishna anything troubling your heart, and receive personalized guidance based on relevant verses from the Bhagavad Gita.

**Example Query:** "I am worried about my job"

**Krishna's Response:**
> Hey Vats,
> 
> "Perform your prescribed duty, for doing so is better than not working. One cannot even maintain one's physical body without work." This is a message I shared with Arjuna when he was filled with doubt and concern.
> 
> I understand your worries about your job; it is a common concern for many. Remember that focusing on your duties is essential, not only for your own well-being but also for the balance of the world around you...

---

## Architecture

### Two-Stage RAG System
```
User Query
    ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 STAGE 1: SEMANTIC RETRIEVAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ↓
OpenAI Embeddings (text-embedding-3-small)
    ↓
ChromaDB Vector Search
    ↓
Top 10 Relevant Verses Retrieved
    ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 STAGE 2: LLM RE-RANKING & GENERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ↓
GPT-4o-mini Analyzes All 10 Verses
    ↓
Selects Most Relevant 1-3 Verses
    ↓
Generates Empathetic Response
    • First-person voice (Krishna speaking)
    • References Mahabharata context
    • Connects ancient wisdom to modern problem
    ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Final Response to User
```

**Why Two Stages?**
- **Stage 1 (Embeddings):** Fast retrieval, ~70% relevance
- **Stage 2 (LLM):** Intelligent selection, boosts to ~85% relevance
- **Combined:** Best of speed + accuracy

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Vector Database** | ChromaDB | Store and search verse embeddings |
| **Embeddings** | OpenAI text-embedding-3-small | Convert text to semantic vectors |
| **LLM** | GPT-4o-mini | Re-rank verses + generate responses |
| **Frontend** | Streamlit | Web interface |
| **Backend** | Python 3.11+ | Core logic |
| **Deployment** | Streamlit Cloud | Hosting |
| **Data Source** | Bhagavad Gita (Prabhupada) | Krishna's direct teachings |

---

## Current Performance

**Metrics (v1.0):**
- **Response Quality:** 60-70% relevance (manual eval on 10 queries)
- **Response Time:** ~3-4 seconds
- **Database:** ~250 Krishna-only verses (filtered from 700)
- **Target:** 85%+ relevance with evals + memory

**Test Categories:**
- Heartbreak & relationship issues 
- Career & work stress 
- Life purpose & meaning 
- Anger & emotional pain 
- Fear & anxiety 

---

## Key Features

### 1. **Empathetic AI Voice**
- Krishna speaks in first person
- Acknowledges user's pain
- Provides hope and support

### 2. **Contextual Storytelling**
- References Arjuna's dilemmas from Mahabharata
- Makes ancient wisdom relatable
- Connects stories to modern problems

### 3. **Verse-Grounded Responses**
- All guidance backed by Gita verses
- Quotes original teachings
- No hallucination - only authentic wisdom

### 4. **Smart Verse Selection**
- Two-stage retrieval for accuracy
- LLM evaluates relevance before responding
- Filters out irrelevant matches

---

## Installation & Local Setup
```bash
# Clone the repository
git clone https://github.com/Rakshit-Lodha/talktokrishna-app.git
cd talktokrishna-app

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your OPENAI_API_KEY to .env

# Run locally
streamlit run app.py
```

**Requirements:**
- Python 3.11+
- OpenAI API key
- ~500MB disk space (for ChromaDB)

------------

## How It Works

### Data Pipeline

**1. Verse Collection**
```python
# Started with 700 verses from Bhagavad Gita
# Filtered to Krishna's direct teachings only
# Result: ~250 high-quality verses
```

**2. Embedding Creation**
```python
# Batch process all verses
embeddings = create_embeddings_batch(
    texts=krishna_verses,
    model="text-embedding-3-small"
)
# Store in ChromaDB for fast retrieval
```

**3. Query Processing**
```python
def ask_krishna(query):
    # Stage 1: Semantic search
    top_10 = chromadb.query(query, n_results=10)
    
    # Stage 2: LLM re-ranking
    response = gpt4o_mini.generate(
        prompt=f"""
        Select most relevant verses from: {top_10}
        Generate empathetic response as Krishna
        Include Mahabharata story context
        """
    )
    return response
```

---

## Example Interactions

### Career Stress
**User:** "I'm stressed about work deadlines"

**Krishna:** Guides on duty without attachment to results (Karma Yoga)

---

### Heartbreak
**User:** "My girlfriend left me"

**Krishna:** References detachment, pain as teacher, and Arjuna's despair on the battlefield

---

### Life Purpose
**User:** "What is the meaning of life?"

**Krishna:** Explains selfless action, dharma, and spiritual growth through Gita wisdom

-------

## 💬 Contact

**Built by:** Rakshit Lodha

**Connect:**
- GitHub: [@Rakshit-Lodha](https://github.com/Rakshit-Lodha)
- LinkedIn: [https://www.linkedin.com/in/rakshit-lodha-360241187/]
- Twitter: [https://x.com/RAKSHITLODHA]

**Feedback?** Open an issue or reach out directly!

---

*"Just as a lamp in a windless place does not flicker, so the disciplined mind of a yogi remains steady in meditation." - Bhagavad Gita 6.19*

---

**⭐ If this project helped you, consider starring the repo!**

**🔗 Try it live:** [talktokrishna-app.streamlit.app](https://talktokrishna-app.streamlit.app/)
