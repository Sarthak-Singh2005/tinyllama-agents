import ollama
print("="* 45)

print("Tinyllama Chatbot")
print("="*45)
print("Enter the question you want to ask the chatbot (type 'exit' to exit)")

message_count = 0;

while True:
    user_input = input("You: ").strip()
    message_count+=1
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break

    if not user_input:
        print("Please type a message.")
        continue

    print("Chatbot is thinking...")

    response = ollama.chat(
        model='tinyllama',
        messages=[
            {'role': 'user', 'content': user_input}
        ]
    )

    ai_Reply = response['message']['content']
    print(f"Chatbot: {ai_Reply}\n")