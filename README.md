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
see: https://tinyurl.com/yczh4373
 - Health Check for the microservice - nice-to-have, but this is needed on for e.g. AWS on microservice startup as an 
 automated check
 
 # Ways to improve this (starting with easiest/most helpful)
  - Flask is a development server and not meant for production. In production we should use a proper production WSGI,
  such as waitress. See: https://tinyurl.com/yyfrzsbw
  - Create a web page to allow users to access on their browser (e.g. in html)
  - Add threading for if there's multiple requests at once  
  - Run on aws ec2 to make this accessible when hosting on the local machine is not possible
  - Spin up on docker to be sure same environment is deployed everywhere - for if this is deployed to prod servers
  - use AWS Fargate in IaC to auto scale based on demand
  - Create a database (e.g. sqlite) and do the heavy lifting of url shortening (create database ID record, encode that 
  record to produce a shortened url) ourselves instead of using an external API. This is more coding but much safer as 
  we don't rely on external services that can be stopped at any time. See: https://tinyurl.com/zl2vh3f
