import time
from selenium import webdriver

filename = 'd:/chromedriver.exe'
driver = webdriver.Chrome(filename) # 드라이버 파일 실행

url = 'http://www.google.com'
driver.get(url) # 드라이버 url 요청

search_textbox = driver.find_element_by_name('q') # find source

word = '북미정상회담'
search_textbox.send_keys(word)
search_textbox.submit()

wait = 5 # 대기 시간
print(str(wait)+ '동안 대기')
time.sleep(wait)

imagefile = 'capture.png'
driver.save_screenshot(imagefile)
print(imagefile + ' 파일로 저장됩니다.')

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('브라우저 종료합니다.')