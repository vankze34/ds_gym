from flask import Flask, render_template, jsonify, request
from cr import idk

app = Flask(__name__)

@app.route('/', methods=['get'])
def get():
    return render_template('reqres.html')  


@app.route('/getdata', methods=['get'])
def getdata():
    x = request.args.get("team", "", str)
    # print("x:", x)
    y = idk(x)
    # print("y:", y)
    return jsonify(y)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")