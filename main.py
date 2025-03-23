import streamlit as st
from utils import generate_word

st.header('🤡单词记忆生成器:')
with st.sidebar:
    openai_api_key = st.text_input("请输入你的密钥:", type='password')
    st.markdown('[deepseek密钥获取地址](https://platform.deepseek.com/sign_in)')
word = st.text_input('请输入要记忆的单词🐒:')
creativity = st.slider('✨ 请输入单词的创造力'
                       '（数字小说明更严谨，数字大说明更多样',
                       min_value=0.0,
                       max_value=1.0, step=0.1, value=0.6)
submit = st.button("Let`s Go🏃🏃🏃")
if submit and not openai_api_key:
    st.info('请输入你的密钥')
    st.stop()
if submit and not word:
    st.info('请输入要记忆的单词')
    st.stop()
if submit:
    with st.spinner('我正在思考🤔，请等待...'):
        result = generate_word(word, openai_api_key, creativity)
        st.markdown('##### 单词')
        st.write(result.word)
        st.markdown('##### 内容')
        st.write(result.content)