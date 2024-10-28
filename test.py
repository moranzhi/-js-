import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://ggzyfw.fujian.gov.cn",
    "Referer": "https://ggzyfw.fujian.gov.cn/business/list/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "portal-sign": "c1bbda67d8b284ad4ca8391c7185e6cb",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "b-user-id": "307ccdcc-fe54-4bda-1f84-7cd95e9eb982"
}
url = "https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo"
data = {
    "pageNo": 6,
    "pageSize": 20,
    "total": 3259,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2024-04-28 00:00:00",
    "EndTime": "2024-10-28 23:59:59",
    "createTime": [],
    "ts": 1730090180103
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)