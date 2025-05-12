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
```
### Say Hello Tool

Greets the users by name.

```bash
def say_hello(name: str) -> str:
    ...

```

## Setup Instructions
1. Clone the repository:
```bash
git clone <your-repo-url>
cd <project-folder>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .env file: Add your OpenAI API key: 
```bash
OPENAI_API_KEY=your_openai_api_key
```
4. Run the application:
```bash
python main.py
```
