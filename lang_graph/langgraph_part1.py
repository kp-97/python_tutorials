import ollama
import typing
from typing import Annotated, Literal, Any
from langgraph.graph.state import StateGraph, CompiledStateGraph
from langgraph.graph import START, END
from langgraph.graph.message import add_messages
from langgraph.pregel import Pregel
from langgraph.types import Command
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.messages.ai import AIMessage
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

# Connect to local ollama
url = "http://host.docker.internal:11434/"
client = ollama.Client(host = url)

# Load model using function provided by langchain.chat_models
model = "gemma4:12b"
llm = init_chat_model(
    model=model,
    model_provider="ollama",
    base_url=url
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph: CompiledStateGraph = graph_builder.compile()


# 1. Explicitly declare this variable is of type 'State'
user_input = input("Enter a message: ")

# 2. Pass it to invoke
state: dict = graph.invoke({"messages": [{"role": "user", "content": user_input}]})

print(state)
print(type(state["messages"][-1]))
print(state["messages"][-1])
print(state["messages"][-1].content)