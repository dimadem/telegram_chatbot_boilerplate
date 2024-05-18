from openai import OpenAI 
from .tokens import OPENAI_API_KEY 

client = OpenAI(
    api_key = OPENAI_API_KEY,
)

def generate_response(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        max_tokens=1024,
        temperature=0.5,
    )
    print(response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()