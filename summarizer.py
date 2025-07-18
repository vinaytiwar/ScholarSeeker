import openai
openai.api_key = "YOUR_API_KEY"

def summarize_paper(text):
    prompt = f"Summarize the following research abstract in simple language:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']