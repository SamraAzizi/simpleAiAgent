from langchain_core.messages import HumanMessages
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuild import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)