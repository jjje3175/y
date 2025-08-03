import streamlit as st
import time as ti
a=0
if st.button ("スライダー"):
    st.error("エラー**サーバーとの通信がおちました**")
    ti.sleep(5)

    if st.button ("やり直しますか"):
        st.error("エラー**サーバーとの通信がおちました**")