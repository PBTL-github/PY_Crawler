import requests

url = "https://www.baidu.com"

res = requests.get(url)

# 对数据编码
res.encoding = "utf-8"

# 保存数据
with open("百度.html", "wb") as f:
    f.write(res.content)