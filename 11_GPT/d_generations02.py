#이미지 생성
import openai
from matplotlib import pyplot as plt
import io
from PIL import Image
import requests

openai.api_key = "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"
response =openai.Image.create(
  prompt="A picture of two Pekingese puppies together",
  n=5,
  size="256x256"
)

def url_to_image(img_url):
    response = requests.get(img_url)
    img = Image.open(io.BytesIO(response.content))
    return img

images = [url_to_image(img_data['url']) for img_data in response.data]

fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, img in zip(axes, images):
    ax.imshow(img)
    ax.axis('off')

plt.tight_layout()
plt.show()
