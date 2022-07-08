#importing things
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
driver.get("https://pantip.com/topic/31081800")

see_mores = driver.find_elements(By.CLASS_NAME,"see-more") #find all see-more button to render every comment

for bt in see_mores: # loop through all button and click it to render
	driver.execute_script("arguments[0].click();",bt) #WTF, it's magic

main_post = driver.find_element(By.CLASS_NAME,"main-post") # get main-post element

comment_section = driver.find_element(By.ID, "comments-jsrender") # get the comment section

comments = comment_section.find_elements(By.CLASS_NAME,"display-post-wrapper-inner") # get all comment

driver.quit()