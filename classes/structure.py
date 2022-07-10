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
		result = []

		def digger(dct,multiple=False):
			for key,val in dct.items():
				if isinstance(val,dict) and all(map(lambda v : isinstance(v, str),val)):
					result.append(Element(key,val,multiple=multiple))
				elif isinstance(val, list):
					result.append(Element(key,val[0],multiple=multiple))
					return digger(dct[key][0],multiple=True)

		digger(self.structure)

		el_name = list(map(lambda it: it.name,result))

		for item in result:
			for k in item.structure:
				if k in el_name:
					setattr(item,'structure',result[el_name.index(k)].name)

		return result
	
			
class Element:
	'''
	This class will handle how to scrape and details of the element before go to the scraper class
	'''

	def __init__(self,name,details,multiple=False):
		self.name = name
		splitted_name = name.split(':')
		self.element_name = splitted_name[0]
		self.main_type,self.main_identifier = splitted_name[1][:-1].split('[')
		self.structure = details
		self.multiple = multiple

	

