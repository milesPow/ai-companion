import streamlit as st



#页面设置
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    #布局
    layout="centered",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)




#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("进阶品质款：Supherb 吡啶甲酸锌")
st.write("核心含量：每粒含吡啶甲酸锌，对应元素锌约 25mg")
st.write("价格参考：约 70 元 / 180 粒，每日成本约 0.39 元")

#图片
st.image("11.png",width=300)

#音频
st.audio("鸟.mp3")

#视频
st.video("山水.mp4")

#Logo
st.logo("华为.png")

#表格
student_data ={
    "姓名":["王林","李慕婉","贝罗","莫厉海","石潇"],
    "学号":["2026001","2026002","2026003","2026004","2026005"],
    "语文":[33,44,55,66,77],
    "数学":[22,32,43,54,67],
    "英语":[32,54,64,43,23],
    "总分":[87,130,162,163,167]
}
st.table(student_data)

#输入框
title = st.text_input("请输入姓名:")
st.write("The current name is",title)

password = st.text_input("请输入您的密码:",type="password")
st.write("The current password is",password)


#按钮
gender = st.radio("您的性别为:",["男","女","未知"],index=1)
st.write("The current gender is",gender)