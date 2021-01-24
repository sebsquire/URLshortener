'''
Purpose: URL shortening microservice capable of receiving a url in RESTful POST, shortening, and returning a short url
Inputs: URL in "/shorten" call
Outputs: Shortened URL that redirects to correct site when called
'''
from flask import Flask, request
import pyshorteners
app = Flask(__name__)                           # instantiate Flask application


def shorten_url(long_url):
    '''
    purpose: function that shortens urls
    inputs: long url
    outputs: short url that redirects to long url
    '''
    s = pyshorteners.Shortener(timeout=2)
    return s.tinyurl.short(long_url)


@app.route('/health-check', methods=['GET'])
def healthCheck():
    return "OK"


@app.route('/shorten', methods=['POST'])
def shorten():
    incoming_url = request.form['url']
    return shorten_url(incoming_url)


if __name__ == "__main__":
    app.run()
