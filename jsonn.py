from flask import Flask, jsonify

app = Flask(__name__)
count = 0  

@app.route('/index', methods=['GET'])
def hello_world():
    global count
    call_count += 1 

    response_data = {
        "message": "Hello World",
        "call_count": count
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
