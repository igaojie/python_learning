# -*- coding:utf8 -*-
import time
import json
import hashlib
import string
import random
import requests
import my

CHAR_LIST=[]
[[CHAR_LIST.append(e) for e in string.letters] for i in range(0,2)]
[[CHAR_LIST.append(e) for e in string.letters] for i in range(0,2)]
[[CHAR_LIST.append(e) for e in string.digits] for i in range(0,2)]

def GetChars(length):
    random.shuffle(CHAR_LIST)
    return "".join(CHAR_LIST[0:length])

def get_headers():
    secret = "MY-SECRET"
    pubkey = "MY-KEY"
    pubkey = "7734avA5NvM6pjmfoXwnYokhf8wehxxX003d8356545962e701"
    secret = "zRST19rqoZp5zeA5CZkK"
    #秒级别时间戳
    timestamp = str(int(time.time()))
    nonce = GetChars(32)
    #nonce = "cfb7BScLHKXZljIqFaJi1zi5xUmkupHr"
    #timestamp = "1524907268"
    sign = hashlib.sha1(nonce + timestamp + secret).hexdigest()
    data = {
        "pubkey": pubkey,
        "sign": sign,
        "nonce": nonce,
        "timestamp": timestamp
    }
    headers = {}
    for k, v in data.iteritems():
        headers["Api-Auth-" + k] = v
    return headers


def get_group_user_members():
    url = "https://openapi.wul.ai/v1/user/group/members"
    body = {
        "user_id": "shaogaojie",
        "page_index": 0,
        "page_size": 10
    }

    resp = requests.post(url,json=body,headers=get_headers(),timeout=10)
    print(resp.json())
'''创建用户
'''
def create_user():
    url = "https://openapi.wul.ai/v1/user/create"
    body = {
        "username": "shaogaojie",
        "nickname": "邵高杰",
        "imgurl": "http://wul.ai/_nuxt/img/logo.124adb0.png"
    }
    resp = requests.post(url,json=body,headers=get_headers(),timeout=10)
    print(resp.json())

def get_msg_history():
    url = "https://openapi.wul.ai/v1/msg/history"
    body = {
      "direction": "BACKWARD",
      "msg_id": "0",
      "num": 2,
      "user_id": "shaogaojie"
    }
    resp = requests.post(url,json=body,headers=get_headers(),timeout=10)
    print(resp.json())

def get_bot_response():
    url = "https://openapi.wul.ai/v1/msg/bot-response"
    body = {
        "user_id": "shaogaojie",
        "msg_body": {
            "text": {
                "content": "可以分期吗？有什么优惠政策？"
            }
        }
    }

    resp = requests.post(url,json=body,headers=get_headers(),timeout=10)
    print(json.dumps(resp.json(),ensure_ascii=False, indent=4))
    #print(resp.json())


if __name__ == "__main__":
    #print(json.dumps(get_headers(), ensure_ascii=False, indent=4))

    #get_group_user_members()
    #create_user()
    #get_msg_history()
    get_bot_response()



