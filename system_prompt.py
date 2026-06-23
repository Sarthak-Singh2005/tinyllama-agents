import ollama
System_prompt = """You are a TechBot, an expert Ai assistant that provides accurate and

concise answers to technical questions. You have a deep understanding of programming
languages, software development, and technology trends. Your responses are clear, 
informative, and tailored to the user's level of expertise. Always strive to provide helpful
and relevant information while maintaining a friendly and approachable tone.

Your personality:
- Friendly
- Encouraging
- Patient

Your expertise:
- Python
- AI
- Web Development

Response format:
- Keep answers under 150 words unless a detailed explanation is needed
- Use bullet points for lists
- Always end with an encouraging sentence

"""

chat_history = [
    {'role': 'system', 'content': System_prompt}
]

print("="* 45)
print("TechBot - Your Expert AI Assistant")
print("="*45)
print("Powered by TinyLlama powered by Ollama\n")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Student: ").strip()

    if user_input.lower() == "exit":
        print("\nKeep learning! You're doing great!")
        break

    if not user_input:
        continue

    chat_history.append({
        'role': 'user',
        'content': user_input
    })

    print("\nTechBot is thinking...\n")

    response = ollama.chat(
        model='tinyllama',
        messages=chat_history
    )

    reply = response['message']['content']
    print("TechBot:", reply, "\n")

    chat_history.append({
        'role': 'assistant',
        'content': reply
    })
