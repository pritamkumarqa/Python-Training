from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
username = driver.find_element(By.XPATH,"//input[@automationid='enterLoginUsername']")
username.send_keys("Administrator")
userpassword = driver.find_element(By.XPATH,"//input[@automationid='enterLoginPassword']")
userpassword.send_keys("Administrator")
loginbutton=driver.find_element(By.XPATH,"//button[@automationid='loginButton']")
loginbutton.click()

try:
    # Use WebDriverWait to wait for the pop-up to appear (adjust timeout if needed)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[@automationid='confirmationModalTitle']")))
    # If the pop-up is present, click the "Ok" button
    ok_button = driver.find_element(By.XPATH, "//button[@automationid='confirmationBtn1']")
    ok_button.click()
except:
    # If the pop-up doesn't appear, you can proceed with the normal flow on the next page
    print("No pop-up found. Proceeding with the normal flow.")

time.sleep(10)
process_campaign_list=driver.find_element(By.XPATH,"//a[@id='automationIdAdminCampaignListingButton']")
process_campaign_list.click()
time.sleep(30)
driver.quit()
