
from dotenv import load_dotenv
import os
import requests

load_dotenv()

class GPTBot:
    def __init__(self) -> None:
        self.headers = {
            "Authorization": f"Bearer {os.environ['API_KEY']}",
            "Content-Type": "application/json"
        }
        self.url_proxy = f"{os.environ['URL_BASE']}"
        self.model = f"{os.environ['MODEL']}"
        self.messages = [
            {"role": "system", 
             "content": """根据需求，直接返回提供兼容5.2.1版本的ECharts options符合格式的JSON字符串,回复格式如下:
                {
                "title": {
                    "left": "center"
                    },
                "tooltip": {},
                "legend": {
                    "orient": "vertical",
                    "left": "left"
                },
                "series": []
            }，不需要说明解释返回内容，请严格遵循json语法返回。"""}
        ]
        self.data = {
            "model": self.model,
            "messages": self.messages,
            "temperature": 0.4,
            'response_format': {"type": "json_object"},
            "top_p": 0.7
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
        

if __name__ == "__main__":

    chatGPT = GPTBot()
    while True:
        message = input("Input:\n")
        reply = chatGPT.send(message)
        print(f"origin reply:\n{reply}")