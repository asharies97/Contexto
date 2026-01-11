import os
from openai import OpenAI

# The client automatically uses the OPENAI_API_KEY environment variable
# or you can set it directly: client = OpenAI(api_key="YOUR_API_KEY")
client = OpenAI()

models_list = client.models.list()
available_models = sorted([model.id for model in models_list])

print("Available models:")
for model in available_models:
    print(f"- {model}")
