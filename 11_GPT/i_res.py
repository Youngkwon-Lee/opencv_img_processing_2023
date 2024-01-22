import streamlit as st
import openai
# Streamlit 앱의 메인 함수
def main():
    # OpenAI API 키 설정
    openai.api_key = "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"

    st.title('GPT-3.5 호반느 경기 규칙 알아보기')

    # 사용자 입력 필드
    user_input = st.text_area("질문을 입력하세요:", "호반느의 경기 규칙은 어떻게 되는거야")

    # 버튼이 클릭되면 True 반환
    is_generate_clicked = st.button("Generate")

    # 버튼이 클릭되었을 때 실행
    if is_generate_clicked:
        # API를 호출하여 응답을 생성
        response = openai.chat.completions.create(
            model="ft:gpt-3.5-turbo-0613:itsa::8IFC3IOk",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.65,
            max_tokens=811,
            top_p=0.82,
            frequency_penalty=0,
            presence_penalty=0
        )

        # 응답 출력
        st.write(response)


# Streamlit 앱 실행
if __name__ == "__main__":
    main()
