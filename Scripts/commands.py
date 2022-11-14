import streamlit as st
from PIL import Image, ImageFont, ImageDraw 
from instagrapi import Client as cl
from Scripts import instagram as ig
from Scripts import pages as pg
from Scripts import configure as cf
import js2py
import time
import os

#스크립트 실행
def script(param):
    #대중적인 언어인 자바스크립트를 사용하기로 했음
    js2py.eval_js(param)

#유저 팔로우
def follow(user):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #instagram.py 파일의 함수를 불러옴
        ig.follow(user)

        return 'success'
    except Exception as e:
        return e

#유저 언팔로우
def unFollow(user):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #instagram.py 파일의 함수를 불러옴
        ig.unFollow(user)
        
        return 'success'
    except Exception as e:
        return e

#친한 친구 리스트로 추가
def addCloseFriends(user):
    #instagram.py 파일의 함수를 불러옴
    result = ig.closeList(user)
    
    if result == 'success':
        st.success(user + '을(를) 친한 친구 리스트에 추가했어요.')
    else:
        st.error(result)

#친한 친구 리스트에서 삭제
def removeCloseFriends(user):
    #instagram.py 파일의 함수를 불러옴
    result = ig.closeListRemove(user)
    if result == 'success':
        st.success(user + '을(를) 친한 친구 리스트에서 삭제했어요.')
    else:
        st.error(result)
