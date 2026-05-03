# 🌍 City Intelligence AI Agent

An intelligent AI-powered system that provides **real-time city insights** like weather updates 🌦️ and latest news 📰 using **LLMs + tools + APIs**.

Built with **LangChain + Mistral + Streamlit**, this project demonstrates how to create a **tool-using AI agent with real-world capabilities**.

---

## Live Link : [ResearchMind](https://city-intelligence-ai-agent.streamlit.app/) 
## 🚀 Features

* 🌦️ **Live Weather Data**

  * Get real-time temperature, weather conditions, and humidity

* 📰 **Latest City News**

  * Fetch and summarize recent news using Tavily Search API

* 🤖 **AI Agent with Tool Calling**

  * Automatically decides when to use tools

* 🧠 **Conversation Memory**

  * Maintains chat context for better responses

* 💬 **Modern Chat UI**

  * Built with Streamlit (ChatGPT-style interface)

* ⚡ **Real-time API Integration**

  * OpenWeatherMap + Tavily APIs

---

## 🧠 How It Works

<img width="400" height="300" alt="Gemini_Generated_Image_rysny1rysny1rysn" src="https://github.com/user-attachments/assets/620e7bf6-03c2-4dda-9593-5cfb28b7edfb" />

---
👉 The agent:

1. Understands user query
2. Decides whether to use a tool
3. Calls the tool if needed
4. Returns an intelligent response

---

## 🛠️ Tech Stack

* **LLM**: Mistral (via LangChain)
* **Framework**: LangChain
* **Frontend**: Streamlit
* **APIs**:

  * OpenWeatherMap (Weather)
  * Tavily (News Search)
* **Language**: Python

---

## 📂 Project Structure

```bash
├── agents.py              # CLI-based agent system
├── app.py                 # Streamlit frontend (main app)
├── newssummarizer.py      # News summarization pipeline (chain)
├── ownTool.py             # Custom tool example
├── requirements.txt       # Dependencies
└── .env                   # API keys (not included)
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/city-intelligence-ai.git
cd city-intelligence-ai
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Environment Variables

Create a `.env` file:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API_KEY=Your api key
```

---

### 5. Run the App

```bash
streamlit run app.py
```

---

## 💬 Example Queries

* “What’s the weather in Mumbai?”
* “Latest news in Delhi”
* “What’s happening in Bangalore today?”

---

## 🧪 CLI Version (Optional)

Run the terminal-based agent:

```bash
python agents.py
```

---

## 🔥 Key Concepts Demonstrated

* ✅ Tool Calling in LLMs
* ✅ Agent Loop (ReAct-style reasoning)
* ✅ Human-in-the-loop (CLI version)
* ✅ API Integration
* ✅ Chat-based UI
* ✅ Chains vs Agents

---

## Output
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/03677609-d2eb-428b-8ed2-87c7e53e0c98" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3aa2e763-809f-448c-8771-ab6676d153d2" />



---


## ⚠️ Important Notes

* Never expose API keys in code
* Always use `.env` for secrets
* Ensure Tavily API key is valid

---

## 🚀 Future Improvements

* 🧠 Long-term memory (vector DB)
* 🎙️ Voice input/output
* 📊 Analytics dashboard
* 🔐 Tool approval toggle
* 🌐 Deployment (Streamlit Cloud)

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💡 Author

**Mitesh Bhoir**

---

⭐ If you found this helpful, consider giving it a star!
