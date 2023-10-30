from selenium import webdriver

import time

driver=webdriver.Chrome()
#chromedrive executbale path is not provided, selemium automatically downloads it at the below path
# - /Users/pritamkumar/.cache/selenium/chromedriver/mac-arm64/118.0.5993.70/chromedriver and use it by default

print(type(driver))
driver.maximize_window()
driver.get("https://www.google.com")
mytitle = driver.title
print(mytitle)
print(driver.quit)
time.sleep(10)
assert "Google" in mytitle,"Title page assertion failed"   #here we have appied assertion on title
driver.quit()
