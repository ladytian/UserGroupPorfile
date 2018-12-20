# -*- coding:utf-8 -*-
__author__ = 'tianjiwei'
from flask import Flask
from flask import render_template
from getdata import get_wc_data
# import userWordCloud
 
app = Flask(__name__)
 
@app.route('/')
def all():
    return '欢迎开启-基于无线漫游的用户群体画像-的大门'
 
@app.route('/portrait/')
def portrait():
    # wc = userWordCloud.WC()
    # wc.draw_wordcloud()
    return render_template('portrait.html')

@app.route('/getdata/')
def getdata():
	return get_wc_data()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1') 