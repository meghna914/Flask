from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello World!!</h1>"

@app.route('/hello')
def hello():
    return "hey there! welcome to the world of flask!!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}! Hope you are doing well!!"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"<h2>The sum of the two numbers are as follows:</h2>\n{num1} + {num2} = {num1+num2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting}, {name}! :)"
    else:
        return "Some parameters are missing :("

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)