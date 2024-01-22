import openai
import requests

openai.api_key = "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"

response = openai.Image.create_variation(
    image=open("puppy.png", "rb"),
    n=2,
    size="1024x1024"
)

image_urls = [img['url'] for img in response['data']]

for idx, image_url in enumerate(image_urls):
    image_data = requests.get(image_url).content
    with open(f"res/variations_{idx}.png", "wb") as f:
        f.write(image_data)

print("이미지가 성공적으로 저장되었습니다!")


