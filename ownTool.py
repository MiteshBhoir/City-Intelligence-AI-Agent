from langchain.tools import tool

@tool
def get_greeting(name: str) -> str:
    """Generate a greeting message for a user"""
    return f"Hello {name},welcome to AI world"

result =get_greeting.invoke({"name":"mitesh"})
print(result)