from flask import Flask,render_template, request
import utils

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def homepage():
    return render_template("main.html")
    
@app.route("/json",methods=['GET', 'POST'])
def json():
    message = utils.get_requests()
    return utils.get_response(message)
    
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)