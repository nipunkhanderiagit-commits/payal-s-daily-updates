# import ollama

# # test = ollama.chat("llama3.2", "Hello, Ollama")
# test = ollama.chat(model='llama3.2', messaages=[{'role':'user', 'content':'why is sky blue'}])
# print(test)


from ollama import Client
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

print(response)