import re
from datetime import datetime

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    text = '''
    <h1>Hello, Word Flask!</h1>
    <h2>Please, come inside</h2>
    <a href="/hello/<name>">Data</a>
    '''
    return text
            
@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %b, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
print('http://127.0.0.1:5000/hello/JanCode')