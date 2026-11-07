import ollama

reponse = ollama.chat(
    model="qwen2.5-coder:3b",
    messages=[{"role": "user", "content": "Dis bonjour en une phrase."}],
)
print(reponse["message"]["content"])