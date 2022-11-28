# 클릭 매크로: 반응 속도 테스트(https://simritest.com/reaction/)

import pyautogui as auto
#auto.displayMousePosition()

color = (178, 255, 178) # 찾는 색

while True:
    screen = auto.screenshot() # 창 캡쳐
    pos = auto.position() # 마우스 위치 확인
    if screen.getpixel((pos.x, pos.y)) == color: # 만약 마우스 위치의 픽셀이 찾는 색이면
        auto.click(pos.x, pos.y) # 그 좌표에 클릭 시도
