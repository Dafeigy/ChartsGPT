
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
                """请根据需求，直接返回提供兼容5.2.1版本的ECharts options 符合格式的JSON字符串,不需要在回复中对返回内容说明。回复格式如下:{
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
                }"""}
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
        print(response)
        reply = response["choices"][0]["message"]['content']
        self.messages.pop()
        print(reply)
        try:
            return reply
        except:
            print("Acquiring failed.")
            reply = '''
            {
    "title": {
        "left": "center"
    },
    "tooltip": {},
    "legend": {
        "orient": "vertical",
        "left": "left"
    },
    "xAxis": {
        "type": "category",
        "data": [
            "Json",
            "parse",
            "Failed",
            "Please",
            "Contact",
            "me",
            "in Github"
        ]
    },
    "yAxis": {
        "type": "value"
    },
    "series": [
        {
            "type": "line",
            "data": [
                4,
                0,
                4,
                4,
                0,
                4,
                0
            ]
        }
    ]
}
            
            '''
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
