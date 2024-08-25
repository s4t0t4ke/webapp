import streamlit as st

# タブの選択
#st.header("モード変更")
tab = st.radio(
    "",
    ("タブ1", "タブ2", "タブ3"),
    label_visibility="collapsed",
    horizontal=True
)

# サイドバーの内容をタブに応じて変更
with st.sidebar:
    st.header(f"{tab}")
    if tab == "タブ1":
        st.write("これはタブ1用のサイドバーです。")
        slider_value = st.slider("スライダー", 0, 100, 50)
        st.write(f"スライダーの値：{slider_value}")
    elif tab == "タブ2":
        st.write("これはタブ2用のサイドバーです。")
        select_value = st.selectbox("選択ボックス", ["オプションA", "オプションB", "オプションC"])
        st.write(f"選択された値：{select_value}")
    elif tab == "タブ3":
        st.write("これはタブ3用のサイドバーです。")
        a = st.text_area('Please input any strings', height=500)
        if a:
            st.write(a)

# メインコンテンツの表示
if tab == "タブ1":
    st.subheader("これはタブ1の内容です。")
    st.write("ここにタブ1の詳細な情報を表示します。")
elif tab == "タブ2":
    st.subheader("これはタブ2の内容です。")
    st.write("ここにタブ2の詳細な情報を表示します。")
elif tab == "タブ3":
    st.subheader("これはタブ3の内容です。")
    st.write("ここにタブ3の詳細な情報を表示します。")
