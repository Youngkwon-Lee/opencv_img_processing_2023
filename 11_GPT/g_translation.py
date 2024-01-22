import os
import openai
openai.api_key = "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"
audio_file = open("sample02.m4a", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

print(transcript.text)
audio_file.close()

