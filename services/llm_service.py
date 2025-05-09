import os
from constants import LLM_URL, SYSTEM_PROMPT, MODEL_NAME
from openai import OpenAI


def generate_queries_service(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=LLM_URL)

    response = client.chat.completions.create(
        model = MODEL_NAME,
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
    ],
        max_tokens=80,
        temperature=0.3,
        stream=False,
        frequency_penalty=0.2
    )

    return response.choices[0].message.content
