import streamlit as st 
import data
import random

import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_KEY"])


def prepare():
    random.shuffle(data.icon_list)
    random.shuffle(data.role_list)


def make_chat(history, idx):
    model = genai.GenerativeModel('gemini-pro', safety_settings=data.safety_settings)
    talk_history = ""
    for talk in history:
        user = talk.get("role")
        content = talk.get("content")
        if user == "ai":
            continue
        talk_history += f"Agent[0{user}]: {content}\n"
    talk_history += f"{data.icon_list[idx]}: XXX"
    prompt = data.PROMPT.format(idx, talk_history)
    response = model.generate_content(prompt)
    result = response.text
    result = result.replace(" ", "")
    if result[9] == ":":
        result = result[10:]
    return result


def main():
    st.title("私はロボットではありません!")
    st.header("DEMO版")

    # 最初の起動時だけ実行
    if "history" not in st.session_state:
        prepare()
        first = data.FIRST.format(data.icon_list[0], data.role_list[0])
        data.talk_count = 0
        st.session_state["history"] = [{"role": "ai", "content": first}]

    # アプリの再実行の際に履歴のチャットメッセージを表示
    for talk in st.session_state["history"]:
        with st.chat_message(talk["role"]):
            st.markdown(talk["content"])

    # ユーザー入力に対する反応
    if user_input := st.chat_input("入力", max_chars=100):
        if data.talk_count < 3:
            data.talk_count += 1
            # チャットメッセージコンテナにユーザーメッセージを表示
            icon = data.icon_list[0]
            st.chat_message(icon).markdown(user_input)
            # チャット履歴にユーザーメッセージを追加
            st.session_state["history"].append({"role": icon, "content": user_input})
            
            for idx in range(1,5):
                icon = data.icon_list[idx]
                response = make_chat(st.session_state["history"], idx)
                # チャットメッセージコンテナにアシスタントのレスポンスを表示
                st.chat_message(icon).markdown(response)
                # チャット履歴にアシスタントのレスポンスを追加
                st.session_state["history"].append({"role": icon, "content": response})
            if data.talk_count == 3:
                end = "OWARI"
                st.chat_message("ai").markdown(end)
                st.session_state["history"].append({"role": "ai", "content": end})
                # 投票先のボタン表示


if __name__ == "__main__":
    main()