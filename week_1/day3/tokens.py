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
prompt1="Hi"
prompt2="tell me about psychology why we should learn"
prompt3="write a essay 200 words on ai ml"
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:

    message={
        "role":role,
        "content":prompt
    }

    messages=[message]

    response=client.chat.completions.create(model=model,messages=messages, max_tokens=150)
    print(response.choices[0].message.content)
    usage=response.usage
    print(f"Prompt: {prompt} ==> Your Token: {usage.prompt_tokens} , completeion Token: {usage.completion_tokens} , Total Token: {usage.total_tokens}, Finish Reason: {response.choices[0].finish_reason}")

