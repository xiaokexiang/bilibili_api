"""
requests > 2.1.0
如下配置
requests.packages.urllib3.disable_warnings()
requests.get(url, verify=False)
"""
import requests
import json

# 动态API请求的地址
API_URL = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?' \
          'csrf=1150f93e4f2524a119d1aaf1b8d416e8' \
          '&visitor_uid=276689059' \
          '&host_uid=57276677' \
          '&offset_dynamic_id=0' \
          '&need_top=1' \
          '&platform=web'

if __name__ == '__main__':
    #
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'accept-encoding': 'gzip',  # 这里不要填写br压缩
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77 '
    }
    response = requests.get(API_URL, headers=headers)
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
        for card in cards:
            c = card.get('desc')
            if c.get('type') == 64:
                print('url: ', 'https://www.bilibili.com/read/cv' + str(c.get('rid')))
