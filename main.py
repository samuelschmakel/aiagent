import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

resp_object = client.models.generate_content(
    model='gemini-2.0-flash-001', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
print(resp_object.text)
print(f"Prompt tokens: {resp_object.usage_metadata.prompt_token_count}")
print(f"Response tokens: {resp_object.usage_metadata.candidates_token_count}")