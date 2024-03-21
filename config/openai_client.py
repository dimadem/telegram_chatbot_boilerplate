from openai import OpenAI 
from .tokens import OPENAI_API_KEY 

client = OpenAI(
    api_key = OPENAI_API_KEY
)