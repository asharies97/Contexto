import os
from inngest.experimental import ai

print(ai.openai.Adapter(
    auth_key=os.getenv("GEMINI_API_KEY"),
    # Point to Google's OpenAI-compatible base URL
    base_url="https://generativelanguage.googleapis.com/v1beta/",
    model="gemini-1.5-flash"
))