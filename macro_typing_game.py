# 영문 타자연습 매크로
import pyautogui as auto
import pyperclip as clip
from time import sleep

texts = []
while True:
    text = auto.prompt("글을 입력해주세요(아무 입력 없을 시 2초 후 코드가 실행됩니다.)", "타자연습 글쓰기")
    if len(text) > 0:
        texts.append(text)
    else:
        sleep(2)
        while len(texts) > 0:
            auto.write(texts.pop(0)) # 순서대로 팝업
            # 너무 빠르면 엔터 인식을 못함
            sleep(0.1)
            auto.press("Return", interval=0.1)