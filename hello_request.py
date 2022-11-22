import requests

r = requests.get("https://www.baidu.com")

# print(type(r.text))


data = {
    "name": "germey",
    "age": 22
}

res = requests.get("http://httpbin.org/get", params=data)
# print(res.text)

url = "https://www.jianshu.com/p/2fc559e6fa00"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

res1 = requests.get(url, headers=headers)
print(res1.text)
