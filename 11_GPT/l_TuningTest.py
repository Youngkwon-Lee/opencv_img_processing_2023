# This code is for v1 of the openai package: pypi.org/project/openai
import openai
openai.api_key = "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"

response = openai.chat.completions.create(
  model="ft:gpt-3.5-turbo-0613:itsa::8IFC3IOk",
  messages=[
    {
      "role": "user",
      "content": "호반느의 경기규칙은 어떻게 되는거야"
    },
    {
      "role": "assistant",
      "content": "호반느는 두 팀으로 나뉘어 경기를 진행하며, 경기 시간은 일반적으로 45분에서 1시간 정도로 설정됩니다. 경기는 팀원들이 손으로 느를 사용하여 상대 팀의 느를 공격하고 방어하는 것으로 이루어집니다. 상대 팀의 느를 공격하여 느를 뺏거나 상대 팀의 느를 방어하여 골을 막는 팀이 승리합니다."
    },
    {
      "role": "user",
      "content": "경기장은 어떻게 구현되는 거야"
    },
    {
      "role": "assistant",
      "content": "호반느는 일반적으로 실내 체육관이나 야외 경기장에서 진행됩니다. 경기장은 일정한 크기와 형태를 가지며, 두 팀은 경기장을 가로지르는 중앙선을 기준으로 한 쪽을 공격하고 다른 쪽을 방어합니다. 경기장은 보통 느의 공격과 방어를 용이하게 하기 위해 특정한 장치로 구성될 수도 있습니다."
    }
  ],
  temperature=0.65,
  max_tokens=832,
  top_p=0.82,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)