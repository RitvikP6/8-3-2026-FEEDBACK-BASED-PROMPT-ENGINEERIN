from groq import Groq

client = Groq(api_key="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")

def generate_response(prompt, temperature=0.7, max_tokens=512):
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content