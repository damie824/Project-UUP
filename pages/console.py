import streamlit as st
from Scripts import commands as cmd

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
    st.title('Command Console')
    command = st.text_input(label='Commends',label_visibility= 'hidden', placeholder = '작동시킬 커맨드를 입력해주세요.')
    run = st.form_submit_button('Run')
    if run:
        if command.startswith('client.'):
            handler = command[7:len(command)]
            param = handler[9:len(command)]
            if handler.startswith('follow'):
                result = cmd.follow(param)
                if result == 'success':
                    st.success(param + '을(를) 팔로우했어요.')
                else:
                    st.error(result)
            elif handler.startswith('unfollow'):
                result = cmd.unFollow(param)
                if result == 'success':
                    st.success(param + '을(를) 언팔로우했어요.')
                else:
                    st.error(result)
            elif handler.startswith('closeFriend'):
                cmd.addCloseFriends(param)
            elif handler.startswith('removeCF'):
                cmd.removeCloseFriends(param)
            else:
                st.error('명령어를 찾을 수 없어요.')
            
        else:
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