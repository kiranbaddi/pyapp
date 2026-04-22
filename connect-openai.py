from openai import OpenAI

def main():
    client = OpenAI()

    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )

    print(res.choices[0].message.content)  
    
if __name__ == "__main__":
    main()