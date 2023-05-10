import requests
import json

class Chartxt():
    def __init__(self, text, cfg = 'config.json') -> None:
        self.cfg = self.load_cfg(cfg)
        self.headers = self.cfg['headers']
        self.url_proxy = self.cfg['url']
        self.model = self.cfg['model']
        self.messages = [
            {"role": "system", 
             "content": 
             r"""{},请根据需求提供兼容5.2.1版本的ECharts options 符合格式的JSON字符串,回复json格式如下:`{
                title: {
                left: 'center'
                },
                tooltip: {
                },
                legend: {
                orient: 'vertical',
                left: 'left'
                },
                series: [],
                ...
            }`,不需要补充说明返回内容。""".format(text)}
        ]

        self.data = {
            "model": self.model,
            "messages": self.messages
                     }
        
    def load_cfg(self, cfg_file):
        with open(cfg_file,'r', encoding='UTF-8') as f:
            config = json.load(f)
        return config
    
    def send(self):
        req = requests.post(url=self.url_proxy, json=self.data, headers=self.headers)
        response =req.json()
        reply = response["choices"][0]["message"]
        self.messages.append(reply)
        return reply
    
if __name__ == "__main__":
    bot = Chartxt(r"创建一个折线图，横坐标['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']，纵坐标 [150, 230, 224, 218, 135, 147, 260]")
    bot.send()