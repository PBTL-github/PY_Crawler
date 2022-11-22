import requests

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"
    "User-Agent": "asdfasdf"
}


def crawl():
    url = 'https://danjuanfunds.com/djapi/fund/nav/history/161725?page=1&size=20'
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        items = data.get("data").get("items")
        for i in items:
            print(i)


crawl()
