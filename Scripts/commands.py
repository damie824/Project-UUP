import streamlit as st
from Scripts import instagram as ig

#유저 팔로우
def follow(user):
    #하위 코드 실행 시도, 실패 시 execpt를 불러옴
    try:
        ig.follow(user)

        return 'success'
    except Exception as e:
        return e

#유저 언팔로우
def unFollow(user):
    try:
        ig.unFollow(user)
        
        return 'success'
    except Exception as e:
        return e

#친한 친구 리스트로 추가
def addCloseFriends(user):
    result = ig.closeList(user)
    
    if result == 'success':
        st.success(user + '을(를) 친한 친구 리스트에 추가했어요.')
    else:
        st.error(result)

#친한 친구 리스트에서 삭제
def removeCloseFriends(user):
    result = ig.closeListRemove(user)
    if result == 'success':
        st.success(user + '을(를) 친한 친구 리스트에서 삭제했어요.')
    else:
        st.error(result)
