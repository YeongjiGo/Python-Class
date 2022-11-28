import pyautogui as auto
import pyperclip as clip

from time import sleep

# 네이버 창 열기
def set_page(link):
    auto.hotkey("win", "r", interval = 0.1)
    auto.sleep(2)
    auto.write(link)
    auto.press("return", interval=0.5) # enter키 = return키 
    auto.hotkey("alt", "space", "x", interval=0.1)

#1번 예제 : 네이버에서 오늘 날씨 검색하기
value = auto.prompt("검색어를 입력해주세요", "검색어 입력") 
#오늘 날씨라고 입력하기
set_page("http://naver.com")
auto.sleep(3)
clip.copy(value) #오늘 날씨 글씨 복사
auto.sleep(3)
auto.hotkey("ctrl", "v", interval = 0.5)
auto.sleep(3)
auto.press("return", interval=0.1) #네이버에 '오늘 날씨'로 검색한 결과 나옴


'''
#2번 예제 : 네이버에 로그인
user_id = auto.prompt("아이디를 입력해주세요", "아이디 입력")
passwd = auto.password("패스워드를 입력해주세요", '패스워드 입력', mask='?')

set_page("https://nid.naver.com/nidlogin.login") # 로그인 페이지
auto.write(user_id, interval=0.1) # 입력 인터벌 0.1초
auto.press("tab", interval=0.5) # 비밀번호 선택
auto.write(passwd, interval=0.1) # 입력 인터벌 0.1초
auto.press("return", interval=0.5)
'''