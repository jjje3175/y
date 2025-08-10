import streamlit as st
import streamlit as st
import time

st.title("🎉 複数回風船を飛ばす！")

if st.button("🎈 連続で風船を飛ばす"):
    for i in range(3):
        st.balloons()
        time.sleep(1)