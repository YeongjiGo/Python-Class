
import pyautogui as auto
from threading import Thread  # 스레드 처리

while True:
    targets = list(auto.locateAllOnScreen( #일반 두더지
        "mol_head.png", confidence=0.7)) 
    targets += list(auto.locateAllOnScreen( # 대장 두더지
       "big_mol.png", confidence=0.8))

    for target in targets:
        pos = auto.center(target)
        Thread(target=auto.click, args=(pos, )).start()
'''
#느리게 클릭하는 버전
import pyautogui as auto
cycle = 0
while True:
    targets = list(auto.locateAllOnScreen(
        "mol_head.png", confidence=0.7)) # 두더지 머리/# confidence 는 신뢰도 로서 0~1사이의 값을 넣어주면 됨
    #targets += list(auto.locateAllOnScreen(
    #    "big_mol.png", confidence=0.8)) # 대장 두더지
    
    for target in targets:
        pos = auto.center(target) #사진의 중간 좌표 
        auto.click(pos) # 클릭

'''