import ollama
import json 
import datetime 
import random
import math
import re

MODEL_NAME = "qwen2.5:3b"

#Datetime tool
def get_current_datetime():
    """Return current date and time"""
    now = datetime.datetime.now()
    return now.strftime("Date: %A,%d-%B-%Y | Time: %I:%M %p")

#Calculator tool
def calculate_expression(expression):
    """Evaluate a mathematical expression."""

    try:
        safe_names = {
            k: v
            for k, v in math.__dict__.items()
            if not k.startswith("_")
        }

        result = eval(
            expression,
            {"__builtins__": {}},
            safe_names
        )

        return (
            f"Result of '{expression}' = "
            f"{round(result, 6)}"
        )

    except Exception as e:
        return f"Math error: {str(e)}"

def word_count(text):
    """Counts words, characters and sentences."""

    words = len(text.split())

    chars = len(text)

    chars_no_space = len(
        text.replace(" ", "")
    )

    sentences = (
        text.count(".") +
        text.count("!") +
        text.count("?")
    )

    return (
        f"Words: {words} | "
        f"Characters: {chars} | "
        f"Chars(no spaces): {chars_no_space} | "
        f"Sentences: {sentences}"
    )
    
    # Quiz tool
def generate_quiz(topic):
    """Generates quiz questions."""

    questions = {

        "python": [

            "What does len() do in Python?",

            "What is the difference between a list and tuple?",

            "What is a dictionary in Python?",

            "What does import do in Python?"
        ],

        "ai": [

            "What is supervised learning?",

            "What does LLM stand for?",

            "What is overfitting?",

            "What is a neural network?"
        ],

        "general": [

            "What is RAM?",

            "What does CPU stand for?",

            "What is an API?",

            "What is open-source software?"
        ]
    }

    topic_lower = topic.lower()

    if "python" in topic_lower:

        q = random.choice(
            questions["python"]
        )

    elif (
        "ai" in topic_lower or
        "ml" in topic_lower
    ):

        q = random.choice(
            questions["ai"]
        )

    else:

        q = random.choice(
            questions["general"]
        )

    return (
        f"Quiz question on '{topic}': {q}"
    )


#Tool descriptions for agent
TOOLS = {

    "get_current_time":
        get_current_datetime,

    "calculate":
        calculate_expression,

    "word_count":
        word_count,

    "generate_quiz":
        generate_quiz
}

SYSTEM_PROMPT = """
You are an AI assistant with access to tools.

AVAILABLE TOOLS:

1. get_current_time()
- returns current date and time

2. calculate(expression)
- solves mathematical expressions

3. word_count(text)
- counts words and characters

4. generate_quiz(topic)
- generates quiz questions

IMPORTANT RULES:

- If a tool is needed, respond ONLY with JSON.
- Never explain before JSON.
- Never use markdown.
- Never use code blocks.
- JSON must always be valid.

FORMAT:

{"tool":"tool_name","args":{"arg":"value"}}

EXAMPLES:

User: What time is it?
Assistant:
{"tool":"get_current_time","args":{}}

User: calculate 25*8
Assistant:
{"tool":"calculate","args":{"expression":"25*8"}}

User: count words in hello world
Assistant:
{"tool":"word_count","args":{"text":"hello world"}}

User: give python quiz
Assistant:
{"tool":"generate_quiz","args":{"topic":"python"}}

After tool result is provided,
respond naturally and helpfully.
"""
