#-*- encoding: utf-8 -*-
import os
import openai

# secret key
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an inquisitive interviewer. You will ask me appropriate behavioural interview questions, one at a time. Only ask the following question once I have responded with an example that includes a situation or task, an action, and a result."},
    {"role": "user", "content": "I'm going to apply for the job as a backend developer. the following is my entire job profile including summary, requirements, skills and experiences: Graduated Tech University of Korea, Bachelor's degree in Software Engineering. Took intership programs in Spain in 2023. Took part in e-commerce service development as backend engineer. Has experience in Spring Framework, Django REST Framework."}
  ]
)

print(completion)
print("eol")