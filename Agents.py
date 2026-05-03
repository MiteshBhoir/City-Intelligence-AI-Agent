# First step-Loading all the libraries
from dotenv import load_dotenv

load_dotenv()
import os
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from tavily import TavilyClient

# Now lets create some tools


# Weather tool
@tool
def get_weather(city: str) -> str:
    """Get current weather of a city"""
    API_KEY = "d6b8cb172f544b98566d8c5834606555"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return "City not found"

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return f"{city}: {temp}°C, {weather}, Humidity {humidity}%"


print(get_weather.invoke("Mumbai"))

# Tavily news Tool
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def get_city_news(city: str) -> str:
    """Get latest news about a city"""

    query = f"latest news in {city}"

    response = tavily_client.search(query=query, search_depth="basic", max_results=5)

    results = response.get("results", [])

    if not results:
        return f"No news found for {city}"

    news = []

    for res in results:
        title = res.get("title", "")
        url = res.get("url", "")
        content = res.get("content", "")

        news.append(f"Title : {title} \n Url : {url}\n content : {content[:100]}...")

    return "\n\n".join(news)


print(get_city_news.invoke("mumbai"))

llm = ChatMistralAI(model="mistral-small-2506")
tools = {"get_weather": get_weather, "get_city_news": get_city_news}
llm_with_tool = llm.bind.bind_tools([get_weather, get_city_news])

# Agent loop
messages = []
print("City Intelligence System")
print("Type Exit to quit")

while True:
    user_input = input("you : ")
    if user_input.lower() == "exit":
        break
    messages.append(HumanMessage(content=user_input))

    while True:
        result = llm_with_tool.invoke(messages)
        messages.append(result)
        # if tool is required
        if result.tool_calls:
            for tool_call in result.tool_calls:
                tool_name = tool_call["name"]
                # Human in the loop
                confirm = input(f"Agent wants to call {tool_name} Approve(yes/No)")
                if confirm.lower() == "no":
                    print("Tool call denied and i cannot get the latest information")
                    break
                # execute tool
                tool_result = tools[tool_name].invoke(tool_call)
                messages.append(
                    ToolMessage(content=tool_result, tool_call_id=tool_call["id"])
                )
            continue
        else:
            print(result.content)
