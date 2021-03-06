"""
requests > 2.1.0
如下配置
requests.packages.urllib3.disable_warnings()
requests.get(url, verify=False)
"""
import os
import time
from datetime import date, datetime

from utils import *

if __name__ == '__main__':
    if os.environ.get('CORP_ID') is None \
            or os.environ.get('CORP_SECRET') is None \
            or os.environ.get('TO_USER') is None \
            or os.environ.get('AGENT_ID') is None \
            or os.environ.get('UP_ID') is None \
            or os.environ.get('BARK_TOKEN') is None:
        print('env init error')
        exit(101)
    corp_id = os.environ.get('CORP_ID')
    corp_secret = os.environ.get('CORP_SECRET')
    to_user = os.environ.get('TO_USER')
    agent_id = os.environ.get('AGENT_ID')
    up_id = os.environ.get('UP_ID')
    bark_token = os.environ.get('BARK_TOKEN')
    response = requests.get(str.format(API_URL, up_id), headers=headers, proxies=proxies)
    body = {}
    if response.status_code != 200:
        print('API 请求失败')
        exit(101)
    else:
        cards = list(dict(json.loads(response.text)).get('data').get('cards'))
        """
        type - name
        1:  dynamic_id      comments
        2:  dynamic_id      blog
        4:  dynamic_id_str  text
        64: rid             article
        """
        banner_title = ''
        for card in cards:
            c = card.get('desc')
            _type_ = c.get('type')
            _time_ = c.get('timestamp')
            _now_ = int(time.time())
            title = dict(json.loads(card.get('card'))).get('title')
            banner_url = dict(json.loads(card.get('card'))).get('banner_url')
            article_time = str(datetime.fromtimestamp(_time_))
            if _type_ == 64 and date.fromtimestamp(_now_) == date.fromtimestamp(_time_):
                print("今日推送文章(更新时间：%s) <a href='%s'>%s</a>" % (
                    str(datetime.fromtimestamp(_time_)), URL_PREFIX + str(c.get('rid')), title))
                body['title'] = title
                body['banner'] = banner_url
                body['url'] = URL_PREFIX + str(c.get('rid'))
                banner_title = '今日键圈新闻'
                break
            elif _type_ == 64:
                message = "今日暂无推送！请查看昨日推送文章(更新时间： %s) <a href='%s'>%s</a>" % (
                    article_time, URL_PREFIX + str(c.get('rid')), title)
                print(message)
                body['title'] = title
                body['banner'] = banner_url
                body['url'] = URL_PREFIX + str(c.get('rid'))
                banner_title = '昨日键圈新闻'
                break
        push_bark(body.get('url'), banner_title, bark_token)
