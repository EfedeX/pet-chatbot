from openai import OpenAI
client = OpenAI()


response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="gpt-4o-mini",
)

print(response._request_id)