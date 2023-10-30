from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path="/Users/pritamkumar/PycharmProjects/selenium-chrome-driver/chromedriver/mac-arm64/118.0.5993.70/chromedriver")
driver=webdriver.Chrome(service=s)
print(type(driver))
driver.maximize_window()
driver.get("https://validation.ameyo.com/app/")
mytitle = driver.title
print(mytitle)
print(driver.quit)
time.sleep(5)
assert "Ameyo" in mytitle,"Title page assertion failed"   #here we have appied assertion on title
driver.quit()
