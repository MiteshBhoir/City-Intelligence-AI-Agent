import streamlit as st
from dotenv import load_dotenv
import os
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from tavily import TavilyClient

# ---------------- ENV ---------------- #
load_dotenv()

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="City Intelligence AI",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 City Intelligence System")
st.caption("Weather • News • AI Agent")

# ---------------- TOOLS ---------------- #

@tool
def get_weather(city: str) -> str:
    """Get current weather of a city"""
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return "❌ City not found"

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return f"🌦️ {city}: {temp}°C, {weather}, Humidity {humidity}%"


tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_city_news(city: str) -> str:
    """Get latest news about a city"""
    query = f"latest news in {city}"

    response = tavily_client.search(query=query, search_depth="basic", max_results=5)
    results = response.get("results", [])

    if not results:
        return f"❌ No news found for {city}"

    news = []
    for res in results:
        title = res.get("title", "")
        url = res.get("url", "")
        content = res.get("content", "")

        news.append(f"📰 {title}\n🔗 {url}\n{content[:100]}...\n")

    return "\n".join(news)


# ---------------- LLM ---------------- #

llm = ChatMistralAI(model="mistral-small-2506")
tools = {"get_weather": get_weather, "get_city_news": get_city_news}
llm_with_tools = llm.bind_tools([get_weather, get_city_news])


# ---------------- SESSION STATE ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------- CHAT DISPLAY ---------------- #

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------------- USER INPUT ---------------- #

user_input = st.chat_input("Ask about any city...")

if user_input:
    # show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):

            while True:
                result = llm_with_tools.invoke(st.session_state.messages)
                st.session_state.messages.append(result)

                # TOOL CALL
                if result.tool_calls:
                    for tool_call in result.tool_calls:
                        tool_name = tool_call["name"]
                        args = tool_call["args"]

                        st.write(f"⚙️ Using tool: `{tool_name}`...")

                        tool_result = tools[tool_name].invoke(args)

                        st.session_state.messages.append(
                            ToolMessage(
                                content=tool_result,
                                tool_call_id=tool_call["id"]
                            )
                        )
                    continue

                # FINAL RESPONSE
                else:
                    st.markdown(result.content)
                    st.session_state.chat_history.append(
                        {"role": "assistant", "content": result.content}
                    )
                    break


# ---------------- SIDEBAR ---------------- #

with st.sidebar:
    st.header("⚙️ Settings")

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 💡 Example Queries")
    st.markdown("""
    - Weather in Mumbai
    - Latest news in Delhi
    - What's happening in Bangalore?
    """)


