#step1.selenium 패키지와 time 모듈 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.naver.com/'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_css_selector("input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

#step5.뉴스 탭 클릭
img_capture = pyautogui.locateOnScreen("news.PNG", confidence=0.7)
pyautogui.click(img_capture)
time.sleep(2)

news_titles = driver.find_elements_by_css_selector(".news_tit")

for i in news_titles:
    title = i.text
    print(title)
    href = i.get_attribute('href')
    print(href)