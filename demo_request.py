"""
1. 找地址
2. 发送请求
3. 提取响应
4. 数据入库
"""
import requests
from lxml import etree


def request():
    url_list = [
        "https://blog.csdn.net/weixin_35757704/article/details/121752712",
        "https://36kr.com/p/2006806724780930",
        "https://36kr.com/p/2006799762613123",
        "https://36kr.com/p/2006794845365122"
    ]

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    # for url in url_list:
    #     res = requests.get(url, headers=headers)
    #     tree = etree.HTML(res.text)
    #     # title = html.xpath('//h1[@class="article-title margin-bottom-20 common-width"]/text()')
    #     # title = tree.xpath("//h1")
    #     title = tree.xpath('//h1[@class="title-article"]/text()')
    #     print(title)

    res = requests.get(url_list[0])


request()
