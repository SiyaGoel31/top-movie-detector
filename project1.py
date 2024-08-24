import google.generativeai as genai
import os

text = "which is best movie of 2022?"

genai.configure(api_key="AIzaSyDGKquraJLIKQ38cph8rdFCS6KQbKA08Qg")
generation_config = {"temperature" : 0.9, "top_p":1 , "top_k":1 , "max_output_tokens":2048}  # 100 tokens 75 words
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config )

response = model.generate_content(text)
print(response.text)