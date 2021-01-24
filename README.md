# URL shortener
*Task*

Simple URL shortener microservice, like tinyurl.com or bit.ly.
Required:
 - Request "/shorten" with a URL of their choice returns a unique URL on the service domain. 
 - Visiting this URL redirects to original link

Language: Python
# To Setup
````bash
pip install -r requirements.txt
````

# To test (locally)

Run the program main.py. This starts the flask server locally run this command in a prompt:
````bash
curl http://127.0.0.1:5000/health-check
curl -X POST -F "url=www.google.com/finance/how-to-save.html" http://127.0.0.1:5000/shorten
````

# Features
 - We're currently using the tinyurl api for shortening in the Pyshorteners library, but we could use any of the others,
see https://github.com/ellisonleao/pyshorteners/blob/master/example.py
 - Health Check for the microservice - nice-to-have, but this is needed on for e.g. AWS on microservice startup as an 
 automated check
 
 # ways to improve this
  - Create a database and convert rather than using an API (database? sqlite? how to interact with it encoding? - example?)
  - Create a webpage to do this from (maybe use html - example?)
  - Run on aws ec2 to make this accessible to everyone
  - Spin up on docker to be sure same environment is deployed everywhere
  - use fargate in IaC to auto scale based on demand
  - add threading for if there's multiple requests at once?
