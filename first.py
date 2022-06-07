from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# 크롬드라이버 실행  (경로 예: '/Users/Roy/Downloads/chromedriver')
driver = webdriver.Chrome('chromedriver.exe') 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.google.co.kr/')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(2)

# 검색어 창을 찾아 search 변수에 저장 (css_selector 이용방식)
search_box = driver.find_element_by_css_selector('input.gLFyf.gsfi')


search_box.send_keys('고양이')
search_box.send_keys(Keys.RETURN)
time.sleep(2)


click_box = driver.find_element_by_xpath('/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a')
click_box.click()
time.sleep(2)

img_capture = pyautogui.locateOnScreen("cat.PNG", confidence=0.7)

# pyautogui.moveTo(100, 100)        # 100, 100 위치로 마우스 커서 즉시 이동

print(img_capture)

pyautogui.click(img_capture)