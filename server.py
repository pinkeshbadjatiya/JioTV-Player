import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, Flask
)
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance


url = "https://fr9.seedr.cc/ff_get/771502810/Mirzapur.S02E06.720p.HEVC.x265-MeGusta[eztv.io].mkv?st=yid68hhxGi1zGnFjvwVDGw&e=1603638801"



url_type = 'video/mp4'
#url_type = 'video/webm'
#url_type = "video/mkv"


@app.route("/")
def hello():
    return render_template("index.html", url=url, url_type=url_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True) 
