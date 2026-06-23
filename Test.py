import ollama
response = ollama.chat(
    model="tinyllama",
    messages=[
        {
            "role": "user",
            "content": "write a email for leave"
        }
    ]
)

print(response["message"]["content"])
