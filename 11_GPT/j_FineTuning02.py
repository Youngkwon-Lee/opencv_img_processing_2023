import openai
openai.api_key = openai.api_key = "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"

#print(openai.Model.list())
#print(openai.File.list())
print(openai.FineTuningJob.list(limit= 1 ))# 최신모델의 작업상황

#파인튜닝 모델을 자세히상황확인
#print(openai.FineTuningJob.retrieve( "ftjob-r5kNzLBj89oOpaVLknbYYQfz" ))
#FineTuningJob 의 최신 이벤트 10건 확인
#print(openai.FineTuningJob.list_events( id = "ftjob-r5kNzLBj89oOpaVLknbYYQfz" , limit= 1 ))

#작업취소
print(openai.FineTuningJob.cancel("ftjob-r5kNzLBj89oOpaVLknbYYQfz"))



