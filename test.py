import openai
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Please set your OpenAI API key in the environment variable 'OPENAI_API_KEY'")

openai.api_key = API_KEY


def test_gpt4o():
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, can you briefly describe the capabilities of GPT-4-turbo?"}
            ]
        )
        print("Response:", response.choices[0].message['content'])
    except openai.OpenAIError as e:
        print(f"An error occurred: {e}")


test_gpt4o()
