import ollama
import math

SYSTEM_PROMPT = """
You are a ReAct Agent.

Follow this format:

THOUGHT: Think about the problem.
ACTION: Choose a tool if needed.
OBSERVATION: Tool result.
FINAL ANSWER: Answer the user.
"""

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Calculation Error"

chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("=" * 50)
print("ReAct Tool Agent")
print("=" * 50)
print("Available Tool: calculator")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Tool simulation
    if user_input.startswith("calc "):
        expression = user_input[5:]
        result = calculator(expression)

        print("\nTHOUGHT: User wants a calculation.")
        print("ACTION: Use calculator tool.")
        print(f"OBSERVATION: {result}")
        print(f"FINAL ANSWER: The result is {result}\n")
        continue

    chat_history.append(
        {"role": "user", "content": user_input}
    )

    response = ollama.chat(
        model="tinyllama",
        messages=chat_history
    )

    answer = response["message"]["content"]

    print("\n" + answer + "\n")

    chat_history.append(
        {"role": "assistant", "content": answer}
    )