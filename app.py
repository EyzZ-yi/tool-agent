import streamlit as st
from dotenv import load_dotenv
from agent import run_agent

load_dotenv()

st.title("我的 AI 助手")
st.caption("可以查天气、查时间、查我的笔记")
# 初始化对话历史
if "messages" not in st.session_state :
    st.session_state.messages=[]
# 显示历史对话
for msg in st.session_state.messages :
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
# 处理用户输入
if prompt :=st.chat_input("问我点什么") :
    # 显示用户消息
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role" : "user","content":prompt})
     # 调用 agent 处理
    with st.chat_message("assistant"):
        # st.write_stream 接收生成器,一边接收一边显示
        full_response = st.write_stream(run_agent(prompt))
    st.session_state.messages.append({"role": "assistant", "content": full_response})