import streamlit as st
from Scripts import instagram as ig
from Scripts import pages as pg


username = 'YOUR_ID'
password = 'YOUR_PW'

#인스타그램에 로그인하기

# 페이지 구조 설정
st.set_page_config(page_title='Instagram Account Manager', page_icon='./assets/UUP.ico')

ig.login(username, password)

pg.Main()

#아래는 페이지 UI 및 기초 설정 작업입니다.

#스트림릿 기존 HTML 구조 변경(Footer, 서브헤더 삭제 및 버튼 위젯 관리)
css = """
    <style>
        footer {visibility: hidden;}
        .subheader {font-size: 10px;}
        #row-widget stButton {display: inline;}
    </style>
    """
st.markdown(css, unsafe_allow_html=True) 