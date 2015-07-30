import re
import requests

url = 'https://www.crowdfunder.com/browse/deals&template=false'


data = {
    'entities_only':'true',
    'page':'1'
}
html_post = requests.post(url,data=data)
title = re.findall('"card-title">(.*?)</div>',html_post.text,re.S)
for each in title:
    print each