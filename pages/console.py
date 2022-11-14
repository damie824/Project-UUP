import streamlit as st
import instagrapi
from Scripts import configure as cf
from Scripts import instagram as ig
from Scripts import commands as cmd
from Scripts import pages as pg
import js2py

#콘솔 페이지 출력해주는 파일


#페이지 파비콘 및 타이틀 설정
st.set_page_config(
    page_title='Console',
    page_icon='./assets/UUP.ico'
)


#콘솔 입력 창 제작
console = st.empty()

#콘솔 창에 '폼' 타입의 오브젝트 추가, 이 오브젝트로 수행할 동작 설정
with console.form('console'):
    #폼 타이틀 출력
    st.title('Command Console')
    #폼 텍스트 입력 창 출력 및 설정
    command = st.text_input(label='Commends',label_visibility= 'hidden', placeholder = '작동시킬 커맨드를 입력해주세요.')
    #작성 완료 버튼 출력
    run = st.form_submit_button('Run')
    #눌릴 시 트리거될 이벤트 추가
    if run:
        #커맨드 접두사 설정
        if command.startswith('client.'):
            #커맨드 핸들러(본 명령어)를 입력받은 텍스트 중 7번째 글자 이후로 설정
            handler = command[7:len(command)]
            param = handler[9:len(command)]
            #수행할 동작 판단, 각각 알맞은 함수를 commands.py 파일에서 불러옴
            if handler.startswith('run_script'):
                cmd.script(param)
            elif handler.startswith('follow'):
                result = cmd.follow(param)
                #함수 반환값으로 결과 출력
                if result == 'success':
                    st.success(param + '을(를) 팔로우했어요.')
                else:
                    st.error(result)
            elif handler.startswith('unfollow'):
                result = cmd.unFollow(param)
                #함수 반환값으로 결과 출력
                if result == 'success':
                    st.success(param + '을(를) 언팔로우했어요.')
                else:
                    st.error(result)
            elif handler.startswith('closeFriend'):
                cmd.addCloseFriends(param)
            elif handler.startswith('removeCF'):
                cmd.removeCloseFriends(param)
            else:
                #명령어를 찾을 수 없을 시 출력
                st.error('명령어를 찾을 수 없어요.')
            
        else:
            #접두사가 맞지 않을 시 출력
            st.error('커맨드가 잘못되었어요.')


# 스트림릿 기존 HTML 구조 변경
css = """
    <style>
        #css-f2wjzv ehezqtx4 {visibility: hidden;}
        footer {visibility: hidden;}
        .subheader {font-size: 10px;}
    </style>
    """
st.markdown(css, unsafe_allow_html=True) 