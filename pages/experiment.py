import streamlit as st
import instagrapi
from Scripts import configure as cf
from Scripts import pages as pg

#Experiment 페이지 출력해주는 파일

#페이지 파비콘 및 타이틀 설정
st.set_page_config(
    page_title='Experiment',
    page_icon='./assets/UUP.ico'
)

#페이지 타이틀 출력
st.title('Experiment')

#페이지 서브텍스트 출력
st.write('''실험적인 기능들을 넣어 둔 탭이에요.
##''')

#page 파일의 randomComment 함수 불러옴
pg.randomComment()

#페이지 공백 설정
st.write('##')

#page 파일의 spamComment 함수 불러옴
pg.spamComment()

# 스트림릿 기존 HTML 구조 변경
css = """
    <style>
        #css-f2wjzv ehezqtx4 {visibility: hidden;}
        footer {visibility: hidden;}
        .subheader {font-size: 10px;}
    </style>
    """
st.markdown(css, unsafe_allow_html=True) 