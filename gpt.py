import os
import openai
import requests


# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "



response = openai.Completion.create(
model="text-davinci-003",
prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
temperature=0.9,
max_tokens=150,
top_p=1,
frequency_penalty=0,
presence_penalty=0.6,
stop=[" Human:", " AI:"]
)