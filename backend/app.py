from flask import Flask

app = Flask(__name__) 

@app.route('/') #app route tell Flask 

def greeting():
    return 'Flask is awesome'

