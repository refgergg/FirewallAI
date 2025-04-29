from flask import Flask, request
import logging
from datetime import datetime

# define the flask application
app = Flask(__name__)

# configure the logging
logging.basicConfig(filename='requests.log', level=logging.INFO, format='%(message)s')

# this will run before each request. We log every http request in the file
@app.before_request
def logging_requests():
    requesttime = datetime.now().strftime('%d/%b/%Y %H:%M:%S')
    method = request.method
    ip = request.remote_addr
    route = request.path
    headers = request.headers
    body = request.get_data(as_text=True)
    log = f'{ip} - [{requesttime}] "{method} {route} HTTP/1.1" \n{body}'

    app.logger.info(log)



# our homepage
@app.route("/")
def home():
    return "<p>Hello, World!</p>"

# endpoint we gonna test on
@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    return f"login attempt with username: {username} and password: {password}"


# this makes sure it only runs when the file is explicitly run in terminal. 
# the host interfaces are unspecified, thats why its 0.0.0.0 instead of 127.0.0.1 (or other)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)