from instagrapi import Client
from Scripts import configure as cf
import streamlit as st
cl = Client()

#인스타그램 API에 로그인
def login(username, password):
    cl.login(username, password)
    cf.logger(username + "에 로그인을 완료하였습니다.")
    st.session_state['username'] = username
    

#댓글을 입력
def comment(MURL, text):
    try:
        mediaID = cl.media_id(cl.media_pk_from_url(MURL))
        try:
            cl.media_comment(mediaID, text)
            cf.logger('댓글을 입력하였습니다.')

            return True
        except Exception as e:
            return(e)
    except Exception as e:
        return(e)


#이미지 업로드
def uploadImg(id):
    try:
        cl.photo_upload(path=('./worker/' + id + '.jpg'),caption= '새로운 글이 추가되었어요!')
        cf.logger('이미지를 업로드하였습니다.')

        return 'success'
    except Exception as e:
        return e

#DM 보내기
def sendDM(text, username):
    try:
        userId = cl.user_id_from_username(username)
        cl.direct_send(text, [userId])
        cf.logger(username + '에게 메시지를 전송하였습니다.')

        return 'success'
    except Exception as e:
        return e

#유저 팔로우하기
def follow(user):
    try:
        userId = cl.user_id_from_username(user)
        cl.user_follow(userId)
        cf.logger(user + '을(를) 팔로우하였습니다.')

        return 'success'
    except Exception as e:
        return e



#유저 언팔로우하기
def unFollow(user):
    try:
        userId = cl.user_id_from_username(user)
        cl.user_unfollow(userId)
        cf.logger(user + '을(를) 언팔로우하였습니다.')

        return 'success'
    except Exception as e:
        return e


#유저 친한친구리스트 추가
def closeList(user):
    try:
        userId = cl.user_id_from_username(user)
        cl.close_friend_add(userId)

        return 'success'
    except Exception as e:
        return e


#유저 친한친구리스트 삭제
def closeListRemove(user):
    try:
        userId = cl.user_id_from_username(user)
        cl.close_friend_remove(userId)

        return 'success'
    except Exception as e:
        return e