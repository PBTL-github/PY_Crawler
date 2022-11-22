text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""

from lxml import etree

# obj = etree.HTML(text)
#
# print(obj.xpath("//li/a/@href"))
# print(obj.xpath("//li/a/text()"))
#
# print(obj.xpath('//li[@class="item-inactive"]/a/@href'))


# 获取网页图片
import requests
import os
if os.path.exists("img") is False:
    os.mkdir("./img")

res = requests.get("https://cn.bing.com/images/search?q=%E7%99%BE%E5%BA%A6&qs=n&form=QBIR&sp=-1&pq=%E7%99%BE%E5%BA%A6&sc=0-2&cvid=13DAACA14EE740DAAB0BB7D868FFC897&ghsh=0&ghacc=0&first=1&tsc=ImageHoverTitle")
obj1 = etree.HTML(res.text)
html = obj1.xpath('//img[@class="mimg"]/@src')
print(html)

for idx, item in enumerate(html):
    res1 = requests.get(item)
    with open("./img/" + str(idx) + ".jpg", "wb") as f:
        f.write(res1.content)