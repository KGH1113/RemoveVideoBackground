from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time
import pyautogui

frame_cnt_st = int(input("Starting Frame number: "))
frame_cnt_end = int(input("Ending Frame number: "))

driver = webdriver.Chrome(r"/Users/gang-guhyeon1/Desktop/chromedriver")
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get("https://express.adobe.com/ko-KR/tools/remove-background")

time.sleep(1)

for cnt in range(frame_cnt_st, frame_cnt_end+1):
    # driver.find_element(
    #     By.XPATH,
    #     "/html/body/sp-theme/div/cclqt-remove-background//sp-theme/cclqt-workspace/cclqt-image-upload//div/input"
    # ).send_keys(r"/Users/gang-guhyeon1/Desktop/Python/Frame{0}.jpg".format(cnt))

    # driver.find_element(
    #     By.CSS_SELECTOR,
    #     'input[type="file"]'
    # ).get_attribute('id')
    # .send_keys(r"/Users/gang-guhyeon1/Desktop/Python/Frame{0}.jpg".format(cnt))
    
    pyautogui.moveTo(320, 465)
    pyautogui.click()
    time.sleep()

    while True:
        try:
            # imgURL = driver.find_element(
            #     By.XPATH,
            #     "/html/body/sp-theme/div/cclqt-remove-background//sp-theme/cclqt-workspace/section/img"
            # ).get_attribute("src")
            # urllib.request.urlretrieve(imgURL, "Frame{0} - erased_background.png")
            exec = None
        except:
            exec = True
            pass
        if exec:
            break

# 5초후 종료
time.sleep(5)

