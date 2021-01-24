'''
Purpose: URL shortening web app capable of receiving a url in REST API request, shortening, and returning a short
Inputs: URL in "/shorten" call
Outputs: Shortened URL that redirects to correct site when called
Program flow:

'''
from flask import Flask, request
import requests, contextlib
from urllib.request import urlopen
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


app = Flask(__name__)                           # instantiate Flask application


def shorten_url(long_url):
    '''
    purpose: function that shortens urls
    inputs: long url
    outputs: short url that redirects to long url
    '''
    request_url = ('http://tinyurl.com/api-create.php?' +
    urlencode({'url':long_url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


@app.route('/health-check', methods=['GET'])
def healthCheck():
    return "OK"


@app.route('/shorten', methods=['POST'])
def shorten():
    incoming_url = request.form['url']
    u = shorten_url(incoming_url)
    #print(incoming_url)
    return u


if __name__ == "__main__":
    app.run()
