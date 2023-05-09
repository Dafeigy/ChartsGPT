from flask import Flask,render_template, request
from utils import GPTBot 

app = Flask(__name__)
bot = GPTBot(cfg = 'config.json')

@app.route("/",methods=['GET', 'POST'])
def homepage():
    return render_template("main.html")
    
@app.route("/json",methods=['GET', 'POST'])
def json():
    
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)