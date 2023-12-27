import requests
import json
from lxml import etree
index_url = 'https://tieba.baidu.com/p/5475267611'
response = requests.get(index_url).text
selector = etree.HTML(response)
image_urls = selector.xpath('//img[@class="BDE_Image"]/@src')
offset = 1
for image_url in image_urls:
	image_content = requests.get(image_url).content
	with open ('{}.jpg'.format(offset),'wb') as f:
		f.write(image_content)
	offset = offset + 1

