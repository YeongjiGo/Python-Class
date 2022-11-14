import pyautogui
import time
import pyperclip

print(pyautogui.size())

time.sleep(2) # 2초 대기
#print(pyautogui.displayMousePosition()) # 실시간으로 마우스의 위치가 표시됨 (ctrl+C 로 멈춤)
'''
1번 실습
pyautogui.moveTo(958, 1049, 2) # x 958 y 1049 위치로 2초 간 이동

pyautogui.click() # 마우스 좌클릭
pyautogui.click(button = 'right') # 마우스 우클릭 => pyautogui.rightClick() 과 동일
pyautogui.doubleClick() # 더블클릭 => pyautogui.click(clicks=2) 과 동일
pyautogui.click(clicks=3, interval =1) # 3번 클릭, 1초 마다
'''
'''
2번 실습 : 
# 작업표시줄의 메모장을 맨 뒤로 옮기기
time.sleep(2) # 2초 대기
pyautogui.moveTo(958, 1049, 2)
pyautogui.dragTo(1323, 1060, 2)
'''

'''
3번 실습 : pyperclip 모듈로 한글 복사 붙여넣기
pyperclip.copy("안녕하세요")
pyautogui.hotkey('ctrl', 'v')
'''
'''
# 4번 실습 : write, hotkey 함수로 new file 만들어서 mission success! 출력해보기

pyautogui.moveTo(138, 130, 2)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.write("newfile.py")
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.write("print('mission success!')", interval=0.25)
pyautogui.hotkey('ctrl', 's')
pyautogui.sleep(1)
pyautogui.hotkey('ctrl', 'f5')
pyautogui.moveTo(1068, 526, 2)
pyautogui.click()
'''
