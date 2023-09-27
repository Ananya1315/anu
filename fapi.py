from flask import Flask

app = Flask(__name__)
count = 0  # Initialize the call count variable

@app.route('/index', methods=['GET'])
def hello_world():
    global count  
    count += 1  
    return f'Hello World The end point has been called for {call_count} times.'

if __name__ == '__main__':
    app.run(debug=True)
