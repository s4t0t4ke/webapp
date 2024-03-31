import streamlit as st 
import data
import random

import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_KEY"])

def prepare():
    random.shuffle(data.icon_list)
    random.shuffle(data.role_list)


def make_chat(history):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("簡単な挨拶をしてください")
    return response.text


def main():
    st.title("私はロボットではありません!")
    st.header("DEMO版")

    # 最初の起動時だけ実行
    if "history" not in st.session_state:
        prepare()
        first = f"あなたの役職は{data.role_list[0]}です。"
        st.session_state["history"] = [{"role": "ai", "content": first}]

    # アプリの再実行の際に履歴のチャットメッセージを表示
    for talk in st.session_state["history"]:
        with st.chat_message(talk["role"]):
            st.markdown(talk["content"])

    # ユーザー入力に対する反応
    if user_input := st.chat_input("入力", max_chars=100):
        if data.talk_count < 4:
            data.talk_count += 1
            # チャットメッセージコンテナにユーザーメッセージを表示
            icon = data.icon_list[0]
            st.chat_message(icon).markdown(user_input)
            # チャット履歴にユーザーメッセージを追加
            st.session_state["history"].append({"role": icon, "content": user_input})
            
            for i in range(1,5):
                icon = data.icon_list[i]
                with st.spinner('思考中...'):
                    talk_history = [history["content"] for history in st.session_state["history"]]
                    response = make_chat(talk_history)
                # チャットメッセージコンテナにアシスタントのレスポンスを表示
                st.chat_message(icon).markdown(response)
                # チャット履歴にアシスタントのレスポンスを追加
                st.session_state["history"].append({"role": icon, "content": response})
            if data.talk_count == 3:
                end = "owari"
                st.chat_message("ai").markdown(end)
                st.session_state["history"].append({"role": "ai", "content": end})
                # 投票先のボタン


if __name__ == "__main__":
    main()