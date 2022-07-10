#importing things
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from abc import ABC,abstractmethod

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

class Scraper(ABC):
	def __init__(self,url,structure,main_module):
		self.url = url
		self.main_module = main_module
		self.structure = structure
		driver.get(url)

		see_mores = driver.find_elements(By.CLASS_NAME,"see-more") #find all see-more button to render every comment

		for bt in see_mores: # loop through all button and click it to render
			driver.execute_script("arguments[0].click();",bt) #WTF, it's magic
	
	# @abstractmethod
	def pre_scrape(self,*args):
		pass

	def scrape(self):
		for md in self.main_module:
			if md.multiple:
				result = []
				main = driver.find_elements(eval(f'By.{md.main_type.upper()}'),md.main_identifier)
				for el in main:
					temp = {}
					for k,v in md.structure.items():
						t,i = v[:-1].split('[')
						try:
							temp[k] = el.find_element(eval(f'By.{t.upper()}'),i).text
						except Exception as e:
							# print("I Hate Scraping")
							pass
					result.append({md.element_name : temp})
				setattr(md, 'data', result)
			else:
				print(md.name)
				result = {}
				main = driver.find_element(eval(f'By.{md.main_type.upper()}'),md.main_identifier)
				if isinstance(md.structure,str):
					pass
				else:
					for k,v in md.structure.items():
						t,i = v[:-1].split('[')
						result[k] = main.find_element(eval(f'By.{t.upper()}'),i).text

				setattr(md, 'data', result)

		return

	# @abstractmethod
	def post_scrape(self,*args):
		pass