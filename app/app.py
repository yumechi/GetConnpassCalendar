# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

from Service.GetCalender import get_week_date
GET_ARTICLE = 80


@app.route("/")
def hello():
    from datetime import datetime
    return "hello, " + datetime.now().strftime('%Y/%m/%d %H:%M:%S')


@app.route("/connpass_calender")
def get_connpass_calender():
    return get_week_date(mode='c', count=GET_ARTICLE)


@app.route("/colab_calender")
def get_colab_calender():
    return get_week_date(mode='s', count=GET_ARTICLE)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
