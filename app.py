import requests
import json
from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request
import random

#App Creation
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    r = requests.get('https://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote', verify=False)
    quote = r.json()['content']
    return render_template('quote.html', quote=quote)

@app.route('/about')
def about():
    return render_template('about.html')

#Run App
if __name__ == '__main__':
    app.run(debug=True)

