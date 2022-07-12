# Comment Scraper
Comment scraper is a tool to scrape data from website from the structure you provide in .json file. Then the scraper will take the structure.json file and scrape data to its pattern.

# Example
## This is the structure file that you can write with 
`element_name:identifier_type[identifier_name]` To be Main module
After in main module and you can write `{element_name : identifier_type[identifier_name]}`
```
{
	"main_post:class_name[main-post]": {
		"header": "class_name[display-post-title]",
		"body": "class_name[display-post-story]",
		"tags": "class_name[display-post-tag-wrapper]",
		"timestamp": "class_name[display-post-timestamp]"
	},
	"comment_section:id[comments-jsrender]": [
		{
			"comments:class_name[display-post-wrapper-inner]": {
				"body": "class_name[display-post-story]",
				"timestamp": "class_name[display-post-timestamp]"
			}
		}
	]
}
```

## Then put it in [Structurer Class](https://github.com/KhemIngkapat/comment_scraper/blob/main/classes/structure.py) and put Scraper Instance to [Scraper Class](https://github.com/KhemIngkapat/comment_scraper/blob/main/classes/scraper.py)
```
st = Structurer('structure.json')
sc = Scraper('https://pantip.com/topic/31081800', st)

sc.scrape()
```

# Result
```
{
    "main_post": {
        "header": "ทำงาน 9 ปีเงินเดือนควรจะเท่าไหร่",
        "body": "ชีวิตจริงของบางคนจบ food science จากมหาวิทยาลัยของรัฐ ทำงานปีแรก พ.ศ. 2547  ที่บริษัทโรงงานผลิตอาหารชื่อดังและมั่นคงแห่งหนึ่ง\n2547     เงินเดือน 13000\n2548     เงินเดือน 13650   ขึ้น 5%\n2549     เงินเดือน  14469  ขึ้น 6%\n2550     เงินเดือน  15337  ขึ้น 6%\n2551     เงินเดือน   16257  ขึ้น 6% ปรับตำแหน่งได้อีก 3000 รวมเป็น  19257\n              \n2552     เงินเดือน   20412  ขึ้น 6%\n2553     เงินเดือน   21637   ขึ้น 6%\n2554     เงินเดือน   23151   ขึ้น 7 %\n2555     เงินเดือน   24772   ขึ้น 7%\n2556     เงินเดือน   26505    \nบางคนทำงานมา 9 ปีเงินเดือนประมาณ 26505 ซึ่งเงินขึ้นก็ 5-7%  แต่เห็นบางคนทำงานบร้ษัทมา 9-10 ปี เงินเดือน 70000-80000  มีจริงๆใช่ไหมครับ",
        "tags": "มนุษย์เงินเดือน",
        "timestamp": "8 ตุลาคม 2556 เวลา 14:22 น."
    },
    "comment_section": [
        {
            "comments": {
                "body": "ดูดีมาก เพราะ มีไม่กี่บริษัท ที่จะขึ้น เงินเดือนให้ อัตรา คงที่ และ ดีประมาณนี้\n\nแต่ สาเหตุ ที่ไม่ได้เยอะกว่านี้ เพราะไม่ได้ย้ายงาน หรือ ไม่ได้เป็นตำแหน่งที่ หารายได้ให้กับ บริษัท\n\nย้ายงานกันที เพิ่มที 20-30% หรือ ตำแหน่งที่มีผลกับรายได้หลัก ขอขึ้นเงินเดือนกันง่ายๆ เลย",
                "timestamp": "8 ตุลาคม 2556 เวลา 14:27 น."
            }
        },(and more)
```
