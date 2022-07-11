from classes.structure import Structurer,Element
from classes.scraper import Scraper
import json
st = Structurer('structure.json')
sc = Scraper('https://pantip.com/topic/31081800', st)

sc.scrape()


# print(sc.main_module[1].data)

with open('result.json','w',encoding='utf8') as json_file:
	json.dump(sc.output,json_file,indent=4,ensure_ascii=False)
