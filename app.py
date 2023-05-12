from flask import Flask,render_template, request, jsonify
import json
import utils

app = Flask(__name__)
Bot = utils.GPTBot('config.json')


@app.route("/",methods=['GET', 'POST'])
def homepage():
    return render_template("main.html")
    
@app.route("/json",methods=['GET', 'POST'])
def response():
    global response_
    response = Bot.send(user_input['user-input'])
    
    response_ = Bot.parse_reply(response)
    print(response_)
    return jsonify(response_)
    

@app.route("/ajax",methods=['POST','GET'])
def ajax():
    global user_input
    user_input = request.json
    print(user_input['user-input'])
    return user_input



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)