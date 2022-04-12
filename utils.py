"""
基于企业微信推送
文档地址：https://work.weixin.qq.com/api/doc/90000/90135/90248
1. 先去企业微信管理端创建应用
2. 查找如下配置
corpid: 企业微信组织ID https://work.weixin.qq.com/wework_admin/frame#profile
corpsecret: 企业微信应用密钥(注意保密) 应用详情页面secret按钮
touser: 接收信息的用户（@all 或者 具体用户的企业微信账号，通讯录目录可看）
agentid: 应用ID（应用详情页面可找到） https://work.weixin.qq.com/wework_admin/frame#apps/createApiApp
"""
import json

import requests

from config import *


def push_bark(url, title, token):
    requests.get('https://api.day.app/{0}/{1}?url={2}'.format(token, title, url))


def push_wx(news, corp_id, corp_secret):
    print('prepare to push message!')
    push_news(news, get_access_token(corp_id, corp_secret))


def get_access_token(corp_id, corp_secret):
    resp = requests.post(GET_TOKEN, headers=headers, proxies=proxies, data=json.dumps({
        "corpid": corp_id,
        "corpsecret": corp_secret
    }))
    if resp.status_code != 200:
        print('获取access_token失败')
        exit(101)
    return json.loads(resp.text).get('access_token')


def push_news(news, access_token):
    if access_token is None:
        print('access_token不能为None')
        exit(101)
    resp = requests.post(str.format(PUSH_MESSAGE, access_token), headers=headers, proxies=proxies,
                         data=json.dumps(news))
    if dict(json.loads(resp.text)).get('errmsg') == 'ok':
        print('push message success!')
    else:
        print('push message fail!')
