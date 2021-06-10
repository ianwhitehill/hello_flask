from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"

@app.route('/Dojo')
def another():
    return "Dojo"

@app.route('/say/<name>')
def sayHi(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:times>/<text>')
def textRepeater(text, times):
    return (f"{text} " * times)

if __name__=="__main__":
    app.run(debug= True)