import streamlit as st
import time
import random as rd
x=rd.randint(1,10)
st.title ("ユーザー情報表示ページ")
# session_stateからデータを取得
if 'user_name' in st.session_state.user_name:
    st. success (f"こんにちは、{st.session_state.user_name}さん！")
    st.write("メインページで入力された名前が正しく表示されています。")
    # 追加の表示
    st.balloons() #祝福のアニメーション
if x <=2:
    st. success (f"こんにちは、{st.session_state.user_name}さん！")
    st.write("メインページで入力された名前が正しく表示されています。")
    for i in range(3):
        st.balloons()
        time.sleep(1)
else:
    st.error("ユーザー名が設定されていません")
    st.write("メインページで名前を入力してください")
    for i in range(3):
        st.balloons()
        time.sleep(1)