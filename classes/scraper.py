#importing things
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from abc import ABC

## Setup chrome options
edge_options = Options()
edge_options.add_argument("--headless") # Ensure GUI is off

# Set path to chromedriver as per your configuration
# homedir = os.path.expanduser("~")
webdriver_service = Service(f"./msedgedriver")

# Choose Chrome Browser
driver = webdriver.Edge(service=webdriver_service, options=edge_options)

class Scraper(ABC):
	def __init__(self,url,structure):
		self.url = url
		self.main_module = structure.main_module
		self.structure = structure.structure
		driver.get(url)

		see_mores = driver.find_elements(By.CLASS_NAME,"see-more") #find all see-more button to render every comment

		for bt in see_mores: # loop through all button and click it to render
			driver.execute_script("arguments[0].click();",bt) #WTF, it's magic
	
	# @abstractmethod
	def pre_scrape(self,*args):
		pass

	def scrape(self):
		for md in self.main_module: # for loop every main_module
			if md.multiple:
				result = []
				main = driver.find_elements(eval(f'By.{md.main_type.upper()}'),md.main_identifier) # find all main_module
				for el in main:# for loop every main_module
					temp = {}
					for k,v in md.structure.items():# get the sub_module:some element that require
						t,i = v[:-1].split('[')
						try: #sometimes it has ad
							temp[k] = el.find_element(eval(f'By.{t.upper()}'),i).text
						except Exception as e:
							# print("I Hate Scraping")
							continue
					if temp:# deling with ad
						result.append({md.element_name : temp})
					else:
						pass
				setattr(md, 'data', result) # set attribute to the main_module class
			else: # not multiple main_module
				result = {}
				main = driver.find_element(eval(f'By.{md.main_type.upper()}'),md.main_identifier)# find main_module
				#tbh this need to be fix because it is not flexible with some complex structure
				if isinstance(md.structure,str):#some main_module have only another main_module
					list_element_name = list(map(lambda it : it.name,self.main_module))
					val_class = self.main_module[list_element_name.index(md.structure)]
					result = val_class
				else:
					for k,v in md.structure.items():
						t,i = v[:-1].split('[')
						result[k] = main.find_element(eval(f'By.{t.upper()}'),i).text

				setattr(md, 'data', result)
		driver.quit()

		out = {}

		# for loop the stucture to reconstruct
		for k in self.structure:
			list_element_name = list(map(lambda it : it.name,self.main_module))
			sel_el = self.main_module[list_element_name.index(k)]
			# print(sel_el.data)
			try:
				out[sel_el.element_name] = sel_el.data.data
			except AttributeError:
				out[sel_el.element_name] = sel_el.data

		self.output = out

	# @abstractmethod
	def post_scrape(self,*args):
		pass
