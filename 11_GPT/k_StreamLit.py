import streamlit as st # 모바일 웹앱을 테스트하는 모듈
import openai

openai.api_key="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"
def main():
     system_text = st.text_area("AI 어시스턴트 설정", value="당신은 어시스턴트 AI입니다.")
     user_text = st.text_area("질문", value="GPT 프로그래머의 삶을 알려줘",)
     is_generate_clicked = st.button("문장 생성")

     if is_generate_clicked:
         message = [{"role": "system", "content": system_text}, {"role": "user", "content": user_text}]
         response = openai.ChatCompletion.create(
             model="gpt-3.5-turbo",
             messages=message,
             max_tokens=2000,
             temperature=0,
             stream=True
         )

         partial_words=""
         answer = st.empty()

         for chunk in response:
             if chunk and "delta" in chunk["choices"][0] and "content" in chunk["choices"][0]["delta"]:
                 partial_words += chunk["choices"][0]["delta"]["content"]
                 answer.write(partial_words)

if __name__ == "__main__":
     main()