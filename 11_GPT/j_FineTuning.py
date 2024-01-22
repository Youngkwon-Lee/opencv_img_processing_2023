import os
import openai
openai.api_key = "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"
print(openai.Model.list())
response = openai.File.create(file=open("Fine_sample.jsonl", "rb"), purpose="fine-tune")
file_id = response.id
print(response)

#####################파인튜닝 모델 선정
response_job = openai.FineTuningJob.create(training_file=file_id, model="gpt-3.5-turbo-0613")
job_id = response_job.id
print(job_id)
print(openai.File.list(limit = 10))


#1000개의 토큰당 0.002$다. 오늘 환율로 원화로 바꾸면 2.64




