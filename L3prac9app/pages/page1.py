import streamlit as st
st.title("ユーザー情報入力")
# session stateの初期化
if 'user name' not in st .session_state:
    st.session_state.user_name = ""
#ユーザー名の入力
name = st.text_input ("あなたの名前を入力してください")
if st.button("名前在保存"):
    st. session_state. user_name = name
    st.success("名前を保存しました！")
st.write (f"現在保存されている名前：{st.session_state.user_name}")