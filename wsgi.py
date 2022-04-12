import time
from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'Log into the page'