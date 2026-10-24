import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Kaha hai Bhai")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
prompt="you are a famous for giving brand name idea"

system_message={
    "role":"system",
    "content":"i want to open my restuarent give me 5 name"
}

message={
    "role":role,
    "content":prompt
}

messages=[system_message,message]

response=client.chat.completions.create(model=model,messages=messages,temperature=0)

answer=response.choices[0].message.content
print(answer)

