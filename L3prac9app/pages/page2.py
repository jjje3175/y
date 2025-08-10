import streamlit as st
st.title ("ユーザー情報表示ページ")
# session_stateからデータを取得
if 'user_name' in st.session_state.user_name:
    st. success (f"こんにちは、{st.session_state.user_name}さん！")
    st.write("メインページで入力された名前が正しく表示されています。")
    # 追加の表示
    st.balloons() #祝福のアニメーション
else:
    st.error("ユーザー名が設定されていません")
    st.write("メインページで名前を入力してください")