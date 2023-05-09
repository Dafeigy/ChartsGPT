
import sys
import json
import requests


class GPTBot:
    def __init__(self,cfg) -> None:
        self.cfg = self.load_cfg(cfg)
        self.headers = self.cfg['headers']
        self.url_proxy = self.cfg['url']
        self.model = self.cfg['model']
        self.messages = [
            {"role": "system", 
             "content": 
"""请根据需求提供兼容5.2.1版本的ECharts options 符合格式的JSON字符串,回复json格式如下:{
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
}`,不需要说“以下是符合要求的JSON字符串：”"""}
        ]
        self.data = {
            "model": self.model,
            "messages": self.messages
                     }
    
    def send(self, message:str):
        self.messages.append(
            {"role": "user",
             "content": message}
        )
        req = requests.post(url=self.url_proxy, json=self.data, headers=self.headers)
        response =req.json()
        reply = response["choices"][0]["message"]['content']
        self.messages.pop()
        try:
            reply = json.loads(reply[3:-3])
        except:
            reply = 'Parsing Error'
        return reply
    

    def load_cfg(self, cfg_file):
        with open(cfg_file,'r', encoding='UTF-8') as f:
            config = json.load(f)
        return config

if __name__ == "__main__":

    chatGPT = GPTBot(cfg = 'config.json')
    while True:
        message = input("Input:\n")
        reply = chatGPT.send(message)
        print(reply)
