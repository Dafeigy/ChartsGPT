from flask import Flask,render_template, request
import json
import utils

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def homepage():
    return render_template("main.html")
    
@app.route("/json",methods=['GET', 'POST'])
def response():
    # message = utils.get_requests()
    # return utils.get_response(message)
    return json.dumps(
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
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]
    },
    "yAxis": {
        "type": "value"
    },
    "series": [
        {
            "type": "line",
            "data": [
                150,
                230,
                224,
                218,
                135,
                147,
                260
            ]
        }
    ]
}
    )
    

@app.route("/ajax",methods=['POST','GET'])
def ajax():
    message = request.json
    return message



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)