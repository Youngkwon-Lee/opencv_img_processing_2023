import subprocess

OPENAI_API_KEY = "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"

command = (f'curl https://api.openai.com/v1/models -H '
           f'"Authorization: Bearer {OPENAI_API_KEY}" > listmodel.json')
process = subprocess.run(command, shell=True, text=True, capture_output=True)

if process.returncode != 0:
    print(process.stderr)
else:
    print("모델 목록이 listmodel.json 파일에 저장되었습니다.")
