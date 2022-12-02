import time, datetime
from flask import Flask, render_template

#Must install flask

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'Log into the page'


@app.route('/')
def index():
    fruits = ['apple', 'orange', 'pear']
    timestamp = time.time()
    return render_template(
                    'index.html', 
                    title='My Cool Web Page',
                    content=f'Hello World - {timestamp}',
                    list = fruits
                    )