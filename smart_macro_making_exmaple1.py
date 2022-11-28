import pyautogui as auto
import pyperclip as clip

from time import sleep


windows = auto.getAllWindows()

new_li = ''
for window in windows:
    title = window.title.rstrip() # 타이틀에서 공백 있는 것 제외/rstrip: 문자열 앞뒤 공백 제거
    if title:#공백이면 False, 아니면 True
        new_li +=title


auto.prompt(new_li, "창 확대시키기")
