# 动态API请求的地址 host_uid是up主的id，visitor是账号的id
API_URL = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?' \
          'csrf=1150f93e4f2524a119d1aaf1b8d416e8' \
          '&host_uid={0}' \
          '&offset_dynamic_id=0' \
          '&need_top=1' \
          '&platform=web'
URL_PREFIX = 'https://www.bilibili.com/read/cv'
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'accept-encoding': 'gzip',  # 这里不要填写br压缩
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77 '
}
proxies = {
    'http': 'http://222.74.73.202:42055,http://60.169.241.131:9999,http://218.66.253.145:8800'
}
GET_TOKEN = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
PUSH_MESSAGE = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'
