# 🛡️ ScamCall Shield AI

### AI-Powered Scam Call & Message Detection Platform

ScamCall Shield AI is an intelligent fraud detection platform designed to identify suspicious calls, fraudulent messages, OTP scams, and social engineering attacks using Artificial Intelligence, Machine Learning, Natural Language Processing (NLP), and Large Language Models (LLMs).

The platform analyzes suspicious messages and call transcripts, detects potential fraud patterns, generates risk scores, and provides safety recommendations to help users stay protected from digital scams.

---

## 🚀 Key Features

- **Scam Message Detection:** Analyze SMS and WhatsApp message text to identify potential fraud.
- **Scam Call Analysis:** Analyze recorded call audio or manually provided call transcripts.
- **OTP Scam Detection:** Identify suspicious requests for OTPs, PINs, passwords, and banking credentials.
- **AI Risk Scoring:** Classify suspicious content into Low, Medium, and High risk levels.
- **Explainable AI:** Explain why a message or conversation may be suspicious.
- **Multilingual Support:** Support for English, Kannada, and Hindi.
- **Safety Recommendations:** Provide actionable suggestions to help users avoid potential fraud.
- **Detection History:** Maintain a record of previously analyzed messages and conversations.

## 🧠 How It Works

1. User enters a suspicious message or uploads a call recording.
2. The system extracts and preprocesses the text.
3. NLP and Machine Learning models analyze suspicious patterns.
4. An AI-powered analysis engine evaluates potential scam indicators.
5. The system generates a risk score and classification.
6. Users receive an explanation and recommended safety actions.

## 🏗️ System Architecture

```text
                 USER
                   |
                   v
             React Frontend
                   |
                   v
              FastAPI Backend
                   |
          +--------+---------+
          |                  |
          v                  v
    Text Analyzer       Audio Processor
          |                  |
          v                  v
      NLP Engine         Whisper STT
          |                  |
          +--------+---------+
                   |
                   v
           Scam Detection Engine
                   |
          +--------+---------+
          |                  |
          v                  v
      ML Classifier       Ollama LLM
          |                  |
          +--------+---------+
                   |
                   v
             Risk Analysis
                   |
                   v
         Explanation & Safety Tips
                   |
                   v
             User Dashboard
```

## 🛠️ Technology Stack

### Frontend
- React.js
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Uvicorn

### Artificial Intelligence
- Ollama
- Qwen LLM
- Scikit-learn
- Natural Language Processing
- Sentence Transformers

### Audio Processing
- OpenAI Whisper
- Speech-to-Text

### Database
- SQLite

### Development Tools
- Git
- GitHub
- Visual Studio Code

## 📁 Project Structure

```text
ScamCall-Shield-AI/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   │
│   ├── agents/
│   │   ├── scam_detector.py
│   │   └── risk_analyzer.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── services/
│   │   ├── text_analyzer.py
│   │   ├── audio_processor.py
│   │   └── ollama_service.py
│   │
│   └── models/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       ├── App.jsx
│       └── main.jsx
│
├── dataset/
│
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/manasa-tech/ScamCall-Shield-AI.git
```

```bash
cd ScamCall-Shield-AI
```

### 2. Backend Setup

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn main:app --reload
```

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Start the frontend:

```bash
npm run dev
```

### 4. Ollama Setup

Install Ollama and download the selected model:

```bash
ollama pull qwen3:latest
```

Ensure the Ollama service is running before using AI-powered analysis.

## 🔐 Security and Privacy

- Avoid sharing OTPs, PINs, passwords, or banking credentials.
- Process uploaded recordings only with appropriate consent.
- Do not treat AI predictions as definitive proof of fraud.
- Protect user-uploaded data and sensitive information.
- Provide clear warnings when detection confidence is low.

## 🎯 Project Objectives

- Detect suspicious communication using AI.
- Reduce risks associated with digital fraud.
- Improve awareness of OTP and banking scams.
- Provide understandable explanations of scam indicators.
- Develop an accessible multilingual fraud detection platform.

## 🔮 Future Enhancements

- Real-time scam detection integrations where platform permissions allow.
- Advanced voice-based scam analysis.
- More Indian language support.
- Improved fraud detection models using verified datasets.
- Browser and messaging platform integrations.
- Advanced analytics and fraud pattern monitoring.

## ⚠️ Disclaimer

ScamCall Shield AI is an educational and preventive technology project. Its predictions are probabilistic and may produce false positives or false negatives. It does not guarantee detection of every scam and should not replace official banking, telecom, or law-enforcement reporting channels.

## 👩‍💻 Developer

**Manasa**

GitHub: https://github.com/manasa-tech

---

### Building safer digital communication with Artificial Intelligence. 🛡️
