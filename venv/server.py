from flask import Flask, render_template
import scrapy
import re
import json
import os

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return 'blog'
