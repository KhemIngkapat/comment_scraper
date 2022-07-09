import json

class Structurer:
	'''
	This class will be use to handle the stucture of data from .json file.
	Then this will send data to another class call scraper that will handle
	the simplified of structure and do the scraping jobs.
	'''

	def __init__(self,file_loc:str) -> None:
		with open(file_loc,'r') as json_file:
			self.structure=json.load(json_file)

	@property
	def main_module(self) -> dict:
		result = {}

		def digger(dct):
			for key,val in dct.items():
				if isinstance(val,dict) and all(map(lambda v : isinstance(v, str),val)):
					result[key] = val
				elif isinstance(val, list):
					result[key] = val[0]
					return digger(dct[key][0])

		digger(self.structure)
		for key,val in result.items():
			for k in val:
				if k in result:
					result[key][k] = k

		return result
	
			
class Element:
	'''
	This class will handle how to scrape and details of the element before go to the scraper class
	'''

	def __init__(self,name,**details):
		print(details)

