import openai
from sklearn.linear_model import LogisticRegression #긍/부정 분류기

openai.api_key = "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"

#학습 문장
train_texts = ["I love this product!",
               "This is terrible.",
               "Best purchase ever.",
               "I would not buy this again."]
train_labels = [1, 0, 1, 0]

#새로운 테스트 데이터
new_texts = ["Amazing product!", "Not worth my money."]

#데이터 임배딩
train_embeddings = [openai.Embedding.create(
  model="text-embedding-ada-002",
  input=text,
  encoding_format="float"
)['data'][0]['embedding'] for text in train_texts]

#분류기 실행
classifier = LogisticRegression().fit(train_embeddings, train_labels)

# 새로운 데이터 입력해서 임베딩 한다.
new_embeddings = [openai.Embedding.create(
  model="text-embedding-ada-002",
  input=text,
  encoding_format="float"
)['data'][0]['embedding'] for text in new_texts]

# 새로운 데이터 판별
predictions = classifier.predict(new_embeddings)

for text, prediction in zip(new_texts, predictions):
    sentiment = "긍정" if prediction == 1 else "부정"
    print(f'"{text}" 문장은 {sentiment}입니다.')

