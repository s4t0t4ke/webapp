import streamlit as st 
import random

import parameter
import gamedata as gd
from prompt import *

import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro', safety_settings=parameter.safety_settings)


def make_chat(history, idx):
    talk_history = ""
    for talk in history:
        user = talk.get("role")
        content = talk.get("content")
        if user == "ai":
            continue
        talk_history += f"Agent[0{user}]: {content}\n"
    talk_history += f"Agent[0{idx}]: XXX"
    
    prompt = COMMON.format(idx, talk_history)
    with open("check.md", mode="w") as f:
        f.write(prompt)
    response = model.generate_content(prompt)
    result = response.text
    result = result.replace(" ", "")
    if result[9] == ":":
        result = result[10:]
    return result


def main():
    st.title("私はロボットではありません!")

    # 最初の起動時だけ実行
    if "history" not in st.session_state:
        gd.talk_count = 0
        first = FIRST.format("1", gd.role_list[0])
        st.session_state["history"] = [{"role": "ai", "content": first}]
        seer_result = "Agent[02]は人間でした"
        st.session_state["history"].append({"role": "ai", "content": seer_result})

    # アプリの再実行の際に履歴のチャットメッセージを表示
    for talk in st.session_state["history"]:
        with st.chat_message(talk["role"]):
            st.markdown(talk["content"])

    # ユーザー入力に対する反応
    if user_input := st.chat_input("入力", max_chars=100):
        if gd.talk_count < 3:
            gd.talk_count += 1
            # チャット履歴にユーザーメッセージを追加
            idx = "1"
            st.session_state["history"].append({"role": idx, "content": user_input})
            # チャットメッセージコンテナにユーザーメッセージを表示
            st.chat_message(idx).markdown(user_input)
            
            for idx in ["2", "3", "4", "5"]:
                response = make_chat(st.session_state["history"], idx)
                # チャット履歴にアシスタントのレスポンスを追加
                st.session_state["history"].append({"role": idx, "content": response})
                # チャットメッセージコンテナにアシスタントのレスポンスを表示
                st.chat_message(idx).markdown(response)
            if gd.talk_count == 3:
                end = "OWARI"
                st.chat_message("ai").markdown(end)
                st.session_state["history"].append({"role": "ai", "content": end})


if __name__ == "__main__":
    main()
