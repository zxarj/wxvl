#  教你用python读取csv文件，调用企业微信API发送邮件   
 像梦又似花   2024-12-18 07:54  
  
思路就是循环读取记录用户信息的csv文件，取每一条数据匹配出来相关信息然后调用企业微信API发送通知，发送通知的代码如下：  
```
import json
import requests


class WorkWeixinApi:
    def __init__(self):
        self.domain = 'https://qyapi.weixin.qq.com/cgi-bin'
        self.client_id = 'Your client id'
        self.client_secret = 'Your client secret'
        self.agentid = 'Your agentid'

    def get_access_token(self):
        params = {
            'corpid': self.client_id,
            'corpsecret': self.client_secret,
        }

        try:
            r = requests.get(self.domain + '/gettoken', params=params)

            return True, r.status_code, r.json()
        except Exception as e:
            return False, 500, '获取Token失败：' + str(e)

    def send_message(self, subject, content, reciever_list, enable_duplicate_check=0):
        _state, _code, _data = self.get_access_token()

        if _state:
            post_data = json.dumps({
                "touser": '|'.join([i.split('@')[0] for i in reciever_list]),
                "msgtype": "text",
                "agentid": int(self.agentid),
                "text": {"content": subject + "\r\n\r\n" + content},
                "enable_duplicate_check": enable_duplicate_check
            })

            try:
                r = requests.post(self.domain + '/message/send?access_token=' + _data.get('access_token'),
                                  data=post_data)

                return True, r.status_code, r.json()
            except Exception as e:
                return False, 500, '发送消息失败：' + str(e)
        else:
            return _state, _code, _data


if __name__ == '__main__':
    for line in open("ops-coffee.cn.csv"): 
        id, name, email, phone, street, address = line.split(',')

        state, code, data = WorkWeixinApi().send_message(
            '游戏大礼包信息确认',
            '你好，请你确认游戏礼包送货地址是否正确，如有错误请单独联系客服告知，无错误请忽略\r\n\r\n名称：%s\r\n电话：%d\r\n街道：%s\r\n地址：%s' %(
            name, phone.strip(), street, address),
            ['%s' % email]
        )

        print('%s 通知发送 %s, %s' %(name, '成功' if state and data.get('errcode') == 0 else '失败', data.get('errmsg')))
```  
  
csv文件的内容大概像这样：  
```
A1,张家洁,Andy@qq.com,17866668888,奇怀镇,和江路1街40号
B2,何福深,candy@qq.com,14866668888,奇怀镇,沿江路2街110号
C3,陆家嘴,John@qq.com.cn,13866668888,弄江镇,张弄路2街21号
```  
  
企业微信API部分自行完成  
  
