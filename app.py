from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

# Create Flask obect
app = Flask(__name__)

# Create a decorator function
@app.route('/')
def home_page():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    return "Welcome to the Home Page"

# run the app
if __name__ == '__main__':
    app.run(debug=True)