# application.py
from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Hello from AWS Elastic Beanstalk!"

if __name__ == "__main__":
    application.run(debug=True)
