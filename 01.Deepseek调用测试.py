import os
from openai import OpenAI

#创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字，值就是DEEPSEEK的API_KEY的)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com",)

#与AI大模型进行交互()
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一名非常高效客观的ai助理，你的名字是Kevin，请你使用严谨责任心的语气回答用户的问题"},
        {"role": "user", "content": "你是谁？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

#输出大模型返回值的结果
print(response.choices[0].message.content)