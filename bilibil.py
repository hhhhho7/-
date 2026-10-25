import hashlib
import time
import pandas as pd
import csv
wts = int(time.time())
raw_string = f"web_location=333.934&wts={wts}ea1db124af3c7062474693fa704f4ff8"
w_rid = hashlib.md5(raw_string.encode('utf-8')).hexdigest()
import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://www.bilibili.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.bilibili.com/v/popular/all",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"156\", \"Microsoft Edge\";v=\"156\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0"
}
cookies = {
}
url = 'https://api.bilibili.com/x/web-interface/popular'
params = {
    "ps": "20",
    "pn": "1",
    "web_location": "333.934",
    "w_rid": w_rid,
    "wts": wts
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
text = response.json().get('data').get('list')
alldata=[]
all_data = []
for i in text:
    all_data.append({
        '标题': i.get('title', ''),
        '博主': i.get('owner', {}).get('name', '未知'),
        '视频链接': i.get('short_link_v2', '')
    })
df = pd.DataFrame(all_data)
df.to_excel('bilibili.xlsx', index=False)
print("写入 Excel 完成！")


