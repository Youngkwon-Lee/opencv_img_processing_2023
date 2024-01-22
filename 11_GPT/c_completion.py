#대화형

import os
import openai
openai.api_key = "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"
response=openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="고양이에 대해 설명해줘",
  max_tokens=100,
  temperature=0.6
)

print(response.choices[0].text)