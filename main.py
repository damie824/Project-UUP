import streamlit as st
from PIL import Image, ImageFont, ImageDraw 
from instagrapi import Client as cl
from Scripts import instagram as ig
from Scripts import pages as pg
from Scripts import configure as cf
import time
import os


username = 'YOURID'
password = 'YOURPW'

#인스타그램에 로그인하기

# 페이지 구조 설정
st.set_page_config(page_title='Instagram Account Manager', page_icon='./assets/UUP.ico')

#로그인 변수가 존재하는지 확인, 아닐 시 로그인 후 메인 페이지 불러오기
if 'login' not in st.session_state:
    ig.login(username, password)
    st.session_state.login = True

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

#로그를 띄울 콘솔 창 설정
if 'setup' not in st.session_state:
    #콘솔 기존 메시지 전부 삭제
    os.system('cls')

    #"LOGGER" 메시지 띄우기
    print('''\033[96m    ____    ________    ________  _____________________________ 
    |    |   \_____  \  /  _____/ /  _____/\_   _____/\______   \ 
    |    |    /   |   \/   \  ___/   \  ___ |    __)_  |       _/
    |    |___/    |    \    \_\  \    \_\  \|        \ |    |   \ 
    |_______ \_______  /\______  /\______  /_______  / |____|_  /
            \/       \/        \/        \/        \/         \/ 
    \033[37m''')
    print("로그 작성을 시작합니다.")

    #셋업 완료 설정
    st.session_state.setup = True