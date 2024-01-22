import requests
import streamlit as st
import openai
from PyPDF2 import PdfReader
from gtts import gTTS
from PIL import Image
from io import BytesIO

openai.api_key = "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"

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


def generation_img_gpt(text):
    response= openai.Image.create(
        prompt=f"Generate an image based on the following test:  {text}",
        n=1,
        size="512x512"
    )
    image_url = response.data[0].url
    return  image_url

def summarize_with_gpt(text):
    words = text.split(' ')[:1000]
    truncated_text = ' '.join(words)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text: {truncated_text}",
        max_tokens=100
    )

    summarized_text = response.choices[0].text.strip()
    return summarized_text

def translate_text_with_gpt(text, target_language):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following text from English to {target_language}: {text}",
        max_tokens=1500
    )

    translated_text = response.choices[0].text.strip()
    return translated_text

def main():
    st.title('PDF Summarizer and Audio Conversion')

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.write("Extracting text...")
        extracted_text = extract_text_from_pdf(uploaded_file)
        st.write("Extracted Text:")
        st.write(extracted_text)

        if st.button('Summarize'):
            st.write("Summarizing...")
            summarized_text = summarize_with_gpt(extracted_text)
            st.write("Audio Conversion:")
            st.write(summarized_text)


            target_language = "ko"
            translated_text = translate_text_with_gpt(summarized_text, target_language)
            st.write("번역된 텍스트:")
            st.write(translated_text)

            generation_img=generation_img_gpt(translated_text)
            st.write("generation_img")

            image = Image.open(BytesIO(requests.get(generation_img).content))
            st.image(image, caption="Generated Image", use_column_width=True)


            # Generate audio from the translated text
            st.write("Generating audio...")
            tts = gTTS(text=translated_text, lang='ko')  # 번역된 텍스트를 한국어로 음성 변환
            audio_file = r"c:\test\translated_audio.mp3"

            try:
                tts.save(audio_file)
                st.audio(audio_file, format='audio/mp3')
            except PermissionError:
                st.write("Permission denied: Could not save the audio file.")

if __name__ == "__main__":
    main()
