import ollama

url = "http://host.docker.internal:11434"
model = "gemma4:12b"
prompt = "What is Python?"

# Initialize the client with the custom host URL
client = ollama.Client(host=url)

print("Response from Ollama:")

# Generate the response with streaming enabled
response = client.generate(model=model, prompt=prompt, stream=True)

# Iterate directly through the generator
for chunk in response:
    # The official library provides a dictionary structure. 
    # For client.generate(), the text is in chunk['response']
    print(chunk['response'], end='', flush=False)

print()  # Newline at the end