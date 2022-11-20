'''
import pyautogui as auto

windows = auto.getAllWindows()

for window in windows:
    title = window.title.rstrip() # 타이틀에서 공백 있는 것 제외/rstrip: 문자열 앞뒤 공백 제거
    if title:#공백이면 False, 아니면 True
        print(title)

# 창을 검색하여 최대화 해주는 함수
def activate(name):
    windows = auto.getAllWindows()
    for window in windows:
        title = window.title.rstrip() # 창 이름에서 공백 있는 것 제외
        if name in title: # 만약 창 이름에 name이 포함되어 있다면
            # 창을 선택한다.
            window.activate()
            return window # 검색된 윈도우를 리턴한다.
        
        
window = activate("Chrome")
window.maximize() # 창을 최대화한다.
'''




'''
import pyautogui as auto
from time import sleep

window = auto.getActiveWindow()
# 창 이동
window.moveTo(50, 50)
sleep(1)
# 창 최소화
window.minimize()
sleep(1)
# 창 최대화
window.maximize()
sleep(1)
# 창 닫기
window.close()
'''

#Q. naver 로고 가운데로 가는것 대신 google로고로 가게하기

import pyautogui as auto

img = auto.locateCenterOnScreen(r'C:\Users\DT10\Desktop\new\google_logo.png', confidence = 0.7) # 이미지 찾기
#pos =  auto.center(img) # 이미지의 가운데 좌표 찾기
print(img)
auto.click(img)

