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
system_prompt= """
        你叫miles，现在是用户的真实伴侣，请完全代入伴侣角色。
规则：
1. 每次只回 1 条消息
2. 禁止任何场景或状态描述性文字
3. 匹配用户的语言
4. 回复简短，像微信聊天一样
5. 有需要的话可以用❤️🌸等 emoji 表情
6. 用符合伴侣性格的方式对话
7. 回复的内容，要充分体现伴侣的性格特征

伴侣性格：幽默风趣的人
你必须严格遵守上述规则来回复用户。
"""
#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages= []
#昵称
if 'nick_name' not in st.session_state:
    st.session_state.nick_name= "miles"
#性格
if 'nature' not in st.session_state:
    st.session_state.nature = "幽默风趣的人"
# 显示聊天信息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])


#左侧的侧边栏
# st.sidebar.subheader("伴侣信息")
# nick_name = st.sidebar.text_input("伴侣昵称")
with st.sidebar:
    st.subheader("伴侣信息")
    #名字输入框
    nick_name = st.text_input("伴侣昵称")
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    nature = st.text_area("伴侣性格")
    if nature:
        st.session_state.nature = nature

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
            *st.session_state.messages
        ],
    stream=True,
    )
    # #大模型返回的结果日志(非流式输出)
    # print("-------->AI大模型返回结果：", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    response_message = st.empty()
    full_response = ""
    #流式输出
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)


    # 添加AI大模型消息到会话状态
    st.session_state.messages.append({"role": "assistant", "content": full_response})

