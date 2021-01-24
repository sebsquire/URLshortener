'''
Purpose: URL shortening web app capable of receiving a url in REST API request, shortening, and returning a short
Inputs: URL in "/shorten" call
Outputs: Shortened URL that redirects to correct site when called
Program flow:

'''
from flask import Flask

app = Flask(__name__)                           # instantiate Flask application


@app.route('/health-check', methods=['GET'])
def healthCheck():
    return "OK"


@app.route('/shorten', methods=['POST'])
def shorten():
    return "OK shortened"
    # todo make this function


if __name__ == "__main__":
    app.run()
