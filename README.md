# 🧠 CLI AI Assistant with LangChain, LangGraph, and OpenAI

This is a simple command-line AI assistant built using LangChain, LangGraph, and OpenAI. It integrates basic tools (calculator and greeting) and demonstrates how to stream AI responses in real-time using `create_react_agent`.

## 🚀 Features
- Interact with an AI assistant in your terminal.
- Perform basic arithmetic operations.
- Get personalized greetings.
- Stream responses from OpenAI.
- Extendable with your own custom tools.

## 📦 Technologies Used
- `langchain`
- `langchain_openai`
- `langchain_core`
- `langgraph`
- `python-dotenv`
- OpenAI API
- `uv` (for running async-compatible functions in sync contexts)

## 🧰 Tools Included
### Calculator Tool
Performs addition of two numbers.
```python
def calculator(a: float, b: float) -> str:
    ...