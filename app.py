from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_date = datetime.datetime.now()
    is_new_year = current_date.month == 1 and current_date.day == 1
    return render_template('index.html', is_new_year = is_new_year)