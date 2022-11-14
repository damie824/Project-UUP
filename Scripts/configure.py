import time
import random
import string
import os
from PIL import Image, ImageFont, ImageDraw 

#현재 시간을 불러와 로그 메시지와 취합 후 콘솔에 띄움
def logger(logText):
    #Time모듈의 strftime 함수를 사용해 양식 제작 후 출력
    nowTime = time.strftime('%Y-%m-%m %H:%M:%S', time.localtime(time.time()))
    print(nowTime + ' ' + logText)
    #텍스트 파일에 로그 저장
    with open("./log.txt", 'a') as logFile:
        logFile.write(nowTime + ' ' + logText + '\n')

#랜덤으로 쓸 댓글을 골라 줌
def radomComment():
    #여러 댓글들을 모아서 저장해두었음
    comment = ["너무 멋져요!",  "아름다운 사진이에요", "이렇게 웃어본게 얼마만인지 모르겠어요 ㅋㅋ", "ㅋㅋㅋㅋㅋ 너무 귀여워요", "와 개귀여워", "진짜 사랑해요", "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"]
    
    #랜덤으로 골라서 반환
    return random.choice(comment)

#랜덤 아이디 생성
def randomID():
    #랜덤으로 아스키코드 글자 혹은 숫자를 5글자로 취합해 반환
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

#이미지 생성
def genImage(id, text):
    #베이스로 사용할 이미지 불러옴
    img = Image.open('assets/empty.png')
    #폰트로 사용할 파일 불러옴
    font = ImageFont.truetype('Fonts/GmarketSans.ttf', 85)
    #img 변수에 그리겠다고 선언
    draw = ImageDraw.Draw(img)
    #설정한 값에 맞게 글자 입력
    draw.text((750,720), text, (1, 3, 25), font, align='center', anchor = 'mm')
    #편집된 이미지를 worker 폴더에 id.jpg 형식으로 저장
    img.save('./worker/' + id + '.jpg')

#이미지 삭제
def deleteImg(id):
    os.remove('./worker/' + id + '.jpg')
