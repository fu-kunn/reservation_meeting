import streamlit as st
import random
import requests
import json

page = st.sidebar.selectbox("Choose your page", ["users", "rooms"])

if page == "users":
    st.title("APIテスト")
    # フォームの作成
    with st.form(key="user"):
        user_id: int = random.randint(0, 10)
        username: str = st.text_input("ユーザー名", max_chars=12)
        data = {
            "user_id": user_id,
            "username": username
        }
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        st.write("## 送信データ")
        st.json(data)
        st.write("##  レスポンス結果")
        url = "http://127.0.0.1:8000/users"
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.json(res.json())

elif page == "rooms":
    st.title("APIテスト 会議室")
    # フォームの作成
    with st.form(key="user"):
        user_id: int = random.randint(0, 10)
        username: str = st.text_input("ユーザー名", max_chars=12)
        data = {
            "user_id": user_id,
            "username": username
        }
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        st.write("## 送信データ")
        st.json(data)
        st.write("##  レスポンス結果")
        url = "http://127.0.0.1:8000/users"
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.json(res.json())