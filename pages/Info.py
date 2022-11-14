import streamlit as st

#Info 페이지 출력해주는 파일

#페이지 파비콘 및 타이틀 설정
st.set_page_config(
    page_title='INFO',
    page_icon='./assets/UUP.ico'
)

#페이지 타이틀 출력
st.title("👋 반가워요!")

#기타 정보 출력
st.markdown(
    """
    저희 서비스를 사용해 주셔서 감사해요.
    ###
    ### 왜 만들었나요?
    기존에 만들어져 있던 익명 자동화 서비스는 사용하기 너무 어렵다는 단점이 있었어요.
    심지어 제가 만든 건 모듈 오류로 제대로 작동하지도 않을 정도였으니까요.
"""
)

#기타 정보 출력 2
st.write('하지만 지금은 달라요, 이 사이트를 통해 그 익명 서비스를 더욱 빠르고, 간편하게 사용하실 수 있어요.')

#기타 정보 출력 3
st.markdown('''
    ### 
    ### 어떻게 만들어진 거에요?
    - [Streamlit](https://streamlit.io)라이브러리를 사용해 만들어졌어요
    - [Instagrapi](https://adw0rd.github.io/instagrapi/)를 통해 인스타그램 서버에 연결해요
    ###
    ### 어떻게 사용해요?
    - [DOCS](http://daejeon.damie.kr)에 방문해 사용법을 익히실 수 있을 거에요.

    ###
    ### 버그가 발생하였나요?
    - [admin@damie.kr](mailto:admin@damie.kr)로 제보해 주세요!

    ###
    ### Credits
    - [LeeGyuYeon](http://damie.kr): Main Develope
''')

#사이트 저작권 표시 출력
st.write('''##
copyright © 2022, LeeGyuYeon.''')

# 스트림릿 기존 HTML 구조 변경
css = """
    <style>
        #css-f2wjzv ehezqtx4 {visibility: hidden;}
        footer {visibility: hidden;}
        .subheader {font-size: 10px;}
    </style>
    """
st.markdown(css, unsafe_allow_html=True) 