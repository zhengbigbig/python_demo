from flask import render_template

from .. import app

@app.route('/index', methods=['GET'])
def index():
    '''首页'''
    return render_template('index.html')