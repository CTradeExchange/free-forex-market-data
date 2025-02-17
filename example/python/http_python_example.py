import time

import requests	# pip3 install requests
import json

# Extra headers
test_headers = {
    'Content-Type' : 'application/json'
}

'''
将如下JSON进行url的encode，复制到http的查询字符串的query字段里
{"trace" : "python_http_test1","data" : {"code" : "USDJPY","kline_type" : 1,"kline_timestamp_end" : 0,"query_kline_num" : 2,"adjust_type": 0}}
{"trace" : "python_http_test2","data" : {"symbol_list": [{"code": "USDJPY"},{"code": "GOLD"}]}}
{"trace" : "python_http_test3","data" : {"symbol_list": [{"code": "USDJPY"},{"code": "GOLD"}]}}
'''
test_url1 = 'https://quote.alltick.io/quote-b-api/kline?token=3662a972-1a5d-4bb1-88b4-66ca0c402a03-1688712831841&query=%7B%22trace%22%20%3A%20%22python_http_test1%22%2C%22data%22%20%3A%20%7B%22code%22%20%3A%20%22USDJPY%22%2C%22kline_type%22%20%3A%201%2C%22kline_timestamp_end%22%20%3A%200%2C%22query_kline_num%22%20%3A%202%2C%22adjust_type%22%3A%200%7D%7D'
test_url2 = 'https://quote.alltick.io/quote-b-api/trade-tick?token=3662a972-1a5d-4bb1-88b4-66ca0c402a03-1688712831841&query=%7B%22trace%22%20%3A%20%22python_http_test2%22%2C%22data%22%20%3A%20%7B%22symbol_list%22%3A%20%5B%7B%22code%22%3A%20%22USDJPY%22%7D%2C%7B%22code%22%3A%20%22GOLD%22%7D%5D%7D%7D'
test_url3 = 'https://quote.alltick.io/quote-b-api/depth-tick?token=3662a972-1a5d-4bb1-88b4-66ca0c402a03-1688712831841&query=%7B%22trace%22%20%3A%20%22python_http_test3%22%2C%22data%22%20%3A%20%7B%22symbol_list%22%3A%20%5B%7B%22code%22%3A%20%22USDJPY%22%7D%2C%7B%22code%22%3A%20%22GOLD%22%7D%5D%7D%7D'

resp1 = requests.get(url=test_url1, headers=test_headers)
time.sleep(1)
resp2 = requests.get(url=test_url2, headers=test_headers)
time.sleep(1)
resp3 = requests.get(url=test_url3, headers=test_headers)

# Decoded text returned by the request
text1 = resp1.text
print(text1)

text2 = resp2.text
print(text2)

text3 = resp3.text
print(text3)
