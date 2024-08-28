import streamlit as st

def seikika(n):
    if n < 10:
        return 0
    elif n < 30:
        return 20
    elif n < 50:
        return 40
    elif n < 70:
        return 60
    elif n < 90:
        return 80
    elif n < 110:
        return 100
    else:
        return 120

def render(n2):
    n1 = [0, 0, 0, 0, 0]
    XXX = ""
    table = {
        0: "",
        20: "",
        40: "",
        60: "",
        80: "",
        100: "",
        120: ""
    }
    m = [table[k] for k in n2]
    XXX.format(m)
    n3 = []

# 選択肢のリスト
choice = [1, 2, 3, 4, 5]

# 2列に分けてラジオボタンを配置
col1, col2 = st.columns(2)

with col1:
    st.write("a")
    answer1 = st.radio("a", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer2 = st.radio("b", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer3 = st.radio("c", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer4 = st.radio("d", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer5 = st.radio("e", choice, label_visibility="collapsed", horizontal=True)

with col2:
    st.write("a")
    answer6 = st.radio("f", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer7 = st.radio("g", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer8 = st.radio("h", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer9 = st.radio("i", choice, label_visibility="collapsed", horizontal=True)
    st.write("a")
    answer0 = st.radio("j", choice, label_visibility="collapsed", horizontal=True)

# サイドバーに書き込み
with st.sidebar:
    st.write("aaa")
    if name := st.text_input("bbb",label_visibility="collapsed"):
        n1 = seikika((answer1 + answer6 - 2) * 10) 
        n2 = answer2 + answer7
        n3 = answer3 + answer8
        n4 = answer4 + answer9
        n5 = answer5 + answer0
        n = [n1, n2, n3, n4, n5]
    #st.button("create")
    #st.image('image_file_name.jpg')
