import time
import random
import string
import os
from PIL import Image, ImageFont, ImageDraw 

#현재 시간을 불러와 로그 메시지와 취합 후 콘솔에 띄움
def logger(logText):
    nowTime = time.strftime('%Y-%m-%m %H:%M:%S', time.localtime(time.time()))
    print(nowTime + ' ' + logText)
    with open("./log.txt", 'a') as logFile:
        logFile.write(nowTime + ' ' + logText + '\n')

#랜덤으로 쓸 댓글을 골라 줌
def radomComment():
    comment = ["너무 멋져요!",  "아름다운 사진이에요", "이렇게 웃어본게 얼마만인지 모르겠어요 ㅋㅋ", "ㅋㅋㅋㅋㅋ 너무 귀여워요", "와 개귀여워", "진짜 사랑해요", "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"]
    
    return random.choice(comment)

#랜덤 아이디 생성
def randomID():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

#이미지 생성
def genImage(id, text):
    img = Image.open('assets/empty.png')
    font = ImageFont.truetype('Fonts/GmarketSans.ttf', 85)
    draw = ImageDraw.Draw(img)
    draw.text((750,720), text, (1, 3, 25), font, align='center', anchor = 'mm')
    img.save('./worker/' + id + '.jpg')

    return {'result' : 1}

#이미지 삭제
def deleteImg(id):
    os.remove('./worker/' + id + '.jpg')

#금칙어 체크
def checkFwords(text):
    with open('./fwords/fwords.txt', "r", encoding='utf-8') as fwords:
        fwords = fwords.read().split(' ')

    for i in fwords:
        if i in text:
            return True
    
    return False

