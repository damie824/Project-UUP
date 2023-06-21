import streamlit as st

#Info 페이지 출력해주는 파일

#페이지 파비콘 및 타이틀 설정
st.set_page_config(
    page_title='INFO',
    page_icon='./assets/UUP.ico'
)

#페이지 타이틀 출력
st.title("👋 반가워요!")

#기타 정보 출력
st.markdown(
    """
    저희 서비스를 사용해 주셔서 감사드려요!
    \n\n
    ### 이건 뭐 하는 사이트인가요?

    흔히 "대신 전해드립니다"라고 불리는 서비스를 이용해 보셨나요?\n
    이 서비스들은 운영자가 볼 때까지 기다리거나, 내 정체를 아는 운영자 때문에 고민해야 했어요.\n
    하지만 이 사이트와 함께라면, 그런 문제는 이제 고민하실 필요 없어요!\n
    100% 자동으로 운영되기에 운영자를 기다릴 필요 없고,\n
    유저 정보를 저장하지 않기에 정체를 들킬까 봐 무서워할 필요 없어요!\n
    
    ### 
    ### 왜 만든 거에요?

    일단 위에 말한 것처럼, 전 기존 "대신 전해드립니다" 서비스에 불만이 좀 있었어요.\n
    이 이유로 작년부터 "대신 전해드립니다 자동화"를 시도해 왔어요.\n
    이 프로젝트는 제가 진행한 수많은 자동화 프로젝트 중, 가장 쉽고 안정화되었다고 생각했기에\n
    호스팅을 직접 돌려 보기로 결정한 거에요!\n

    ### 
    ### 어떻게 만들어진 거에요?

    - 백엔드, 프론트엔드 모두 파이썬을 사용했어요.\n
    - 인스타그램 API를 통해 인스타그램 서버에 연결해요\n

    ###
    ### 저도 이거 운영하고 싶은데 어떻게 해야 할까요?
    - [Github](https://github.com/damie824/Project-UUP/)에 소스 코드가 공개되어 있어요!
    - [DOCS](https://uup-docs.damie.works/)에서 사용 방법을 확인해 보세요 :)

    ###
    ### 버그가 발생하였나요?
    - [admin@damie.kr](mailto:admin@damie.kr)로 제보해 주세요!

    ###
    ### Credits
    - [Lee Gyu Yeon](http://damie.works): Main Developer
""")

#사이트 저작권 표시 출력
st.write('''##
copyright © 2023, Damie.''')

# 스트림릿 기존 HTML 구조 변경
css = """
    <style>
        #css-f2wjzv ehezqtx4 {visibility: hidden;}
        footer {visibility: hidden;}
        .subheader {font-size: 10px;}
    </style>
    """
st.markdown(css, unsafe_allow_html=True) 