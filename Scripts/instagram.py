from instagrapi import Client
from Scripts import configure as cf
import streamlit as st
import json
cl = Client()

#인스타그램 API에 로그인
def login(username, password):
    #InstaPy 모듈을 이용해 API에 로그인
    cl.login(username, password)
    cf.logger(username + "에 로그인을 완료하였습니다.")

    #유저 이름을 세션에 저장
    st.session_state['username'] = username
    

#댓글을 입력
def comment(MURL, text):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #입력한 URL에서 미디어 ID를 불러옴
        mediaID = cl.media_id(cl.media_pk_from_url(MURL))
        try:
            #미디어 ID를 이용해 댓글 달기
            cl.media_comment(mediaID, text)
            cf.logger('댓글을 입력하였습니다.')

            return True
        except Exception as e:
            return(e)
    except Exception as e:
        return(e)


#이미지 업로드
def uploadImg(id):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #이미지 업로드하기
        cl.photo_upload(path=('./worker/' + id + '.jpg'),caption= '테스트 중이에요!')
        cf.logger('이미지를 업로드하였습니다.')

        return 'success'
    except Exception as e:
        return e

#DM 보내기
def sendDM(text, username):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #입력한 유저 이름으로 유저 ID 불러옴
        userId = cl.user_id_from_username(username)
        #DM 보내기
        cl.direct_send(text, [userId])
        cf.logger(username + '에게 메시지를 전송하였습니다.')

        return 'success'
    except Exception as e:
        #에러값 반환
        return e

#유저 팔로우하기
def follow(user):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #입력한 유저 이름으로 유저 ID 불러옴
        userId = cl.user_id_from_username(user)
        #유저 팔로우하기
        cl.user_follow(userId)
        cf.logger(user + '을(를) 팔로우하였습니다.')

        return 'success'
    except Exception as e:
        #에러값 반환
        return e



#유저 언팔로우하기
def unFollow(user):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #입력한 유저 이름으로 유저 ID 불러옴
        userId = cl.user_id_from_username(user)
        #유저 언팔로우하기
        cl.user_unfollow(userId)
        cf.logger(user + '을(를) 언팔로우하였습니다.')

        return 'success'
    except Exception as e:
        return e


#유저 친한친구리스트 추가
def closeList(user):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #입력한 유저 이름으로 유저 ID 불러옴
        userId = cl.user_id_from_username(user)
        #유저 친한친구리스트에 추가하기
        cl.close_friend_add(userId)

        return 'success'
    except Exception as e:
        return e


#유저 친한친구리스트 삭제
def closeListRemove(user):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        #입력한 유저 이름으로 유저 ID 불러옴
        userId = cl.user_id_from_username(user)
        #유저 친한친구리스트에서 제거하기
        cl.close_friend_remove(userId)

        return 'success'
    except Exception as e:
        return e