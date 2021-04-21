# Bilibili动态推送脚本

---
<p style="text-align: center">
    <img src="https://img.shields.io/badge/create-2021.04.20-brightgreen" alt="2021.04.20"/>
    <img src="https://img.shields.io/badge/python-3.9-blue" alt="python-3.9"/>
    <img src="https://img.shields.io/badge/github%20-workflow-orange" alt="github action"/>
    <img src="https://img.shields.io/badge/License-GPL-yellow" alt="GPL"/>
</p>


## 特别声明
<b>此脚本只用于学习、测试使用，请勿将此项目的任何内容用于商业或非法目的！本人概不负责！</b>

### 准备

- 需要先<a href='https://work.weixin.qq.com/wework_admin/register_wx?from=myhome'>注册企业微信（个人也能注册）</a>

- 需要知道订阅的UP主的ID（浏览器登录状态下打开账户`关注`界面，控制台筛选`followings`请求，查看返回可知）

- 需要在企业微信中<a href='https://work.weixin.qq.com/wework_admin/frame#apps/createApiApp'>注册应用</a>，消息推送基于应用。

### 推送参数配置

Fork [此项目](https://github.com/xiaokexiang/bilibili_api) ，并添加如下`Secret`到<b>`Settings -> Secrets`</b>中：

|    参数     |                             作用                             |
| :---------: | :----------------------------------------------------------: |
|   CORP_ID   | <a href='https://work.weixin.qq.com/wework_admin/frame#profile'>我的企业ID</a> |
| CORP_SECRET |                  上步创建的应用详情界面可查                  |
|   TO_USER   |         通讯录界面可查（可为`@all`全部用户都会受到）         |
|  AGENT_ID   |                  上步创建的应用详情界面可查                  |
|    UP_ID    |                      通过浏览器请求可查                      |

### 推送效果图

![](https://image.leejay.top/FqevfV-0-EujP8ujzBdyQSWFJ2yQ)

### Github Action

- 基于`Github action`实现脚本自动执行，如果不清楚`Github action`，点击[此处](http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)查看入门教程。
- 定时任务执行基于`Cron`，如果不清楚点击[此处](https://leejay.top/post/linux%E4%B8%8Bcron%E5%AE%9A%E6%97%B6%E5%99%A8/)了解。
- 可以自行编辑`.github/workflows/bilibili.yml`中的`cron: '0 1 * * *'`配置来修改脚本的触发事件，
  也可以通过修改`README.md`文件，触发push的操作来执行脚本。

### 帮助文档

- <a href='https://work.weixin.qq.com/api/doc/90000/90135/90248'>企业微信推送文档地址</a>
