from langchain_core.messages import HumanMessages
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuild import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithemtic calculation with number"""
    print("Tool has been called.")
    return f"The su of {a} and {b} is {a+b}"

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome! Im you AI assistant.Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == 'quit':
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessages(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk['agent']:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()

if __name__=="__main__":
    main()
