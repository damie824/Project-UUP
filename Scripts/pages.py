import streamlit as st
import time
from Scripts import instagram as ig
from Scripts import configure as cf
import asyncio

#메인 페이지
def Main():
    st.title("인스타그램 익명 서비스")
    st.write("익명 서비스를 더욱 쉽고 빠르게 이용해 보세요.")
    st.write('##')
    asyncio.run(unknownPicture())
    st.write('##')
    unknownDM()
    st.write('##')
    spamComment()


#익명 포스트 업로드 탭
async def unknownPicture():
    up = st.empty()
    with up.form('up'):
        st.subheader('익명 포스트 업로드')
        message = st.text_input(max_chars=20, label='message',label_visibility= 'hidden', placeholder = '익명으로 작성하실 말을 입력해 주세요!')
        run = st.form_submit_button('작성 완료')
        if run:
            try:
                id = cf.randomID()
                if(cf.checkFwords(message)):
                    cf.genImage(id=id, text=message)
                    result = ig.uploadImg(id=id)
                    cf.deleteImg(id=id)
                    if result == 'success':
                        st.success('업로드를 완료했어요.')
                    else:
                        st.error(result)
                else:
                    st.error("금칙어가 발견되었어요")
            except Exception as e:
                st.error(e)


#익명 다이렉트 메시지 전송 탭
def unknownDM():
    ud = st.empty()
    with ud.form('ud'):
        st.subheader('익명 다이렉트 메시지 전송')
        user = st.text_input(label='Username', placeholder = '메시지를 보낼 대상의 ID를 입력해 주세요!')
        message = st.text_input(max_chars=20, label='Message', placeholder='익명으로 작성하실 말을 입력해 주세요!')
        run = st.form_submit_button('작성 완료')
        if run:
            if(cf.checkFwords(message)):
                result1 = ig.sendDM(text= message, username=user)
                if result1 == 'success':
                    st.success('메시지를 전송했어요.')
                else:
                    ig.follow(user)
                    result2 = ig.sendDM(text= message, username=user)
                    ig.unFollow(user)
                    if result2 == 'success':
                        st.success('메시지를 전송했어요.')
                    else:
                        st.error(result1)
                        st.error(result2)
            else:
                st.error("금칙어가 발견되었어요")


#랜덤 댓글 탭
def randomComment():
    commentForm = st.empty()
    with commentForm.form('comment'):
        st.header('Random Comment Generator')
        st.write('랜덤으로 댓글을 입력합니다.')
        mediaLink = st.text_input(label="Post Link", placeholder="댓글을 달 개시물의 링크를 입력해 주세요.")
        start = st.form_submit_button("Run")
        if start:
            if(cf.checkFwords(mediaLink)):
                result  = ig.comment(mediaLink, cf.radomComment())
                if result == True:
                    st.success('성공적으로 댓글을 전송했습니다.')
                else:
                    st.error(result)
            else:
                st.error("금칙어가 발견되었어요")


#댓글 스패머
def spamComment():
    spamForm = st.empty()
    with spamForm.form('Comment Spammer'):
        st.header('Comment Generator')
        st.write('같은 댓글을 여러 개시물에 한 번에 입력합니다.')
        contents = st.text_input(label='Comment', placeholder='댓글 내용을 입력하세요')
        postLink = st.text_area(label='Post Link', placeholder='댓글을 달 개시글을 입력하세요. 각각의 개시글은 [Enter]로 구분합니다.')
        run = st.form_submit_button('Run')
        if run:
            if(cf.checkFwords(contents)):
                length = len(postLink.split('\n'))
                for i in range(0,length):
                    result = ig.comment(postLink.split('\n')[i], contents)
                    if (result == True):
                        st.success('댓글을 달았습니다.')
                    else:
                        st.error(result)
            else:
                st.error("금칙어가 발견되었어요")