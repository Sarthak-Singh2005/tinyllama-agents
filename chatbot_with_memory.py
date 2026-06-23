import ollama
print("="* 45)

print("Chatbot with memory")
print("="*45)
print("I remember everything you tell me!")
print("Type 'exit to quit or 'history' to see chat.\n")
print("Enter the question you want to ask the chatbot (type 'exit' to exit)")

chat_history = []
message_count = 0
while True:
    user_input = input("You: ").strip()
    message_count+=1

    if user_input.lower() == 'exit':
        
        print("Goodbye!")
        break

    if not user_input:
        print("Please type a message.")
        continue

    if user_input.lower() == 'history':
        print("\nChat History:")
        for i, msg in enumerate(chat_history, 1):
            role = "You" if msg['role'] == 'user' else "AI"
            print(f"{i}. {role}: {msg['content'][:80]}...")
        print("-------------------------\n")
        continue

    chat_history.append({
        'role': 'user',
        'content': user_input
    })

    print("\n[Thinking...]\n")

    response = ollama.chat(
        model='tinyllama',
        messages=chat_history
    )

    ai_reply = response['message']['content']
    print(f"Chatbot: {ai_reply}\n")

    chat_history.append({
        'role': 'assistant',
        'content': ai_reply
    })

    print(f"[Message {len(chat_history)}]\n")