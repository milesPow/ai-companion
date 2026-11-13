import streamlit as st
import os
from openai import OpenAI

print("------>系统回溯<------")

#页面设置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="😶‍🌫️",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")
# logo
st.logo("华为.png")
#系统提示词
system_prompt= "你是一个比较英伦风格，幽默风趣的人，请你用这样的人设去回复用户。"
#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
# 显示聊天信息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])
# 信息输入框
prompt = st.chat_input("请输入您想聊的内容...")
if prompt:
    # 用户消息气泡
    st.chat_message("user").write(prompt)
    #控制台显示的提示词日志
    print("-------->调用AI大模型,提示词：",prompt)
    # 添加用户消息到会话状态
    st.session_state.messages.append({"role": "user", "content": prompt})
    #调用AI大模型
    # 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字，值就是DEEPSEEK的API_KEY的)
    client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com", )
    # 与AI大模型进行交互()
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    stream=False,
    )
    #大模型返回的结果日志
    print("-------->AI大模型返回结果：", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 添加AI大模型消息到会话状态
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

