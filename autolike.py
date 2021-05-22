from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

key = Controller()
i = 0
option = Options()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe", chrome_options=option)
driver.get("https://www.facebook.com/")
elem = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
elem.send_keys("congvochi10@yahoo.com.vn")
time.sleep(2)
elem = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
elem.send_keys("nkdieutrinh2609")
time.sleep(2)
elem.send_keys(Keys.RETURN)
action = ActionChains(driver)

while i < 5:
    time.sleep(5)
    key.press('j')
    key.release('j')
    if i==0:
        i = i +1
        continue
    key.press('l')
    key.release('l')
    key.press(Key.right)
    key.release(Key.right)
    key.press(Key.enter)
    key.release(Key.enter)
    i = i + 1