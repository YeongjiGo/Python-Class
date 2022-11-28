import pyautogui as auto
from threading import Thread  # 스레드 처리

while True:
    pos = auto.locateCenterOnScreen('coin.png') # 이미지 찾기
    auto.moveTo(pos)
    print('이미지 발견: ', pos)

    for target in targets:
        pos = auto.center(target)
        Thread(target=auto.click, args=(pos, )).start()