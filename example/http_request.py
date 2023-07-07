import requests	# pip3 install requests
import json

# 将如下字段信息进行url的encode，复制到url的查询字符串的query里
"""
{"trace":"3baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806","data":{"code":"USDJPY","kline_type":1,"kline_timestamp_end":0,"query_kline_num":2,"adjust_type":0}}
"""

# Base URL being accessed
test_url = 'https://quote.aatest.online/quote-b-api/kline?token=3662a972-1a5d-4bb1-88b4-66ca0c402a03-1688712831841&query=%7B%22trace%22%3A%223baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806%22%2C%22data%22%3A%7B%22code%22%3A%22USDJPY%22%2C%22kline_type%22%3A1%2C%22kline_timestamp_end%22%3A0%2C%22query_kline_num%22%3A2%2C%22adjust_type%22%3A0%7D%7D'

# Extra headers
test_headers = {
    'Content-Type' : 'application/json'
}

resp = requests.get(url=test_url, headers=test_headers)

# Decoded text returned by the request
text = resp.text
print(text)