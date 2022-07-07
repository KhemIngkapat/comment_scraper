import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
driver.get("https://pantip.com/topic/31081800")

comments = driver.find_elements(By.CLASS_NAME, "display-post-story")

for idx,comment in enumerate(comments):
	print(f'comment : {idx} \n\t{comment.text}')

#Wait for 10 seconds
# time.sleep(10)
driver.quit()