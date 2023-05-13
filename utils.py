
import sys
import json
import requests
import re



class GPTBot:
    def __init__(self,cfg) -> None:
        self.cfg = self.load_cfg(cfg)
        self.headers = self.cfg['headers']
        self.url_proxy = self.cfg['url']
        self.model = self.cfg['model']
        self.rule1 = re.compile(r'```(.*?)```',re.S)
        self.rule2 = re.compile(r'```json(.*?)```',re.S)
        self.messages = [
            {"role": "system", 
             "content": 
                """根据需求，直接返回提供兼容5.2.1版本的ECharts options符合格式的JSON字符串,回复格式如下:{
                "title": {
                "left": 'center'
                },
                "tooltip": {
                },
                "legend": {
                "orient": 'vertical',
                "left": 'left'
                },
                "series": [],
                ...
                }，不需要说明解释返回内容，请严格遵循json语法返回。"""}
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
    
    def parse_reply(self,reply):
        results = self.rule2.findall(reply)
        if len(results) == 0:
            results = self.rule1.findall(reply)
            if len(results) == 0:
                return None
        result = results[0]
        return result

    def check_balance(self):
        url = 'https://openai.api2d.net/dashboard/billing/credit_grants'
        res = requests.get(url, headers=self.headers)
        try:
            balance = res.json()['total_available']
        except:
            balance = 0
            print("Getting balance error!")
        return balance

if __name__ == "__main__":

    chatGPT = GPTBot(cfg = 'config.json')
    while True:
        message = input("Input:\n")
        reply = chatGPT.send(message)
        print(f"origin reply:\n{reply}")
        reply_ = chatGPT.parse_reply(reply)
        print(f"Parsed reply:\n{reply_}")
