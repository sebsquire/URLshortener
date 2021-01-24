# URL shortener
*Task*

Simple URL shortener microservice, like tinyurl.com or bit.ly.
Required:
 - Request "/shorten" with a URL of their choice returns a unique URL on the service domain. 
 - Visiting this URL redirects to original link

Language: Python

# To test

For local testing add this code to the bottom of main.py:

if __name__ == "__main__":
    app.run()
this starts the flask server locally run this command in a prompt:

curl http://127.0.0.5000/healthCheck

# todo:
 - flask app
 - curl command
 - requirements to run
 - URL shortener function to some string increasing number (how?)
 - function to redirect link to user's URL (how?)
 - add threading for if there's multiple requests at once?