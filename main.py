import streamlit as st 
import utils
import data


def main():
    st.title('私はロボットではありません')

    # 最初の起動時だけ実行
    if "history" not in st.session_state:
        utils.prepare()
        first = f"あなたの役職は{data.role_list[data.idx]}です。"
        st.session_state["history"] = [{"role": "ai", "content": first}]

    # アプリの再実行の際に履歴のチャットメッセージを表示
    for talk in st.session_state["history"]:
        with st.chat_message(talk["role"]):
            st.markdown(talk["content"])

    # ユーザー入力に対する反応
    if user_input := st.chat_input("入力", max_chars=100):
        # チャットメッセージコンテナにユーザーメッセージを表示
        icon = data.icon_list[0]
        st.chat_message(icon).markdown(user_input)
        # チャット履歴にユーザーメッセージを追加
        st.session_state["history"].append({"role": icon, "content": user_input})
        
        for i in range(4):
            icon = data.icon_list[1]
            with st.spinner('思考中...'):
                response = utils.make_chat(user_input)
            # チャットメッセージコンテナにアシスタントのレスポンスを表示
            st.chat_message(icon).markdown(response)
            # チャット履歴にアシスタントのレスポンスを追加
            st.session_state["history"].append({"role": icon, "content": response})


if __name__ == "__main__":
    main()