non_primitive = [list,dict]

class Element:
	def __init__(self,text):
		self.name,self.cls = text.split(':')
