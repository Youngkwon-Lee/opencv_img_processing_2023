#이미지 생성
import os
import openai
import requests
from PIL import Image
from io import BytesIO

openai.api_key = "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"
response=openai.Image.create(
  prompt="Photo of two baby Pekingese puppies together",
  n=1,
  size="512x512"
)

#image_url = response['data'][0]['url']
image_url = response.data[0].url

response_img = requests.get(image_url)
img = Image.open(BytesIO(response_img.content))
img.show()


