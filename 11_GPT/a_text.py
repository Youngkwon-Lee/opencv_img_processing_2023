import openai

openai.api_key = "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"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Hello, World!",
    max_tokens=50
)

print(response.choices[0].text.strip())

