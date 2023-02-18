from flask import Flask

# Create Flask obect
app = Flask(__name__)

# Create a decorator function
@app.route('/')
def home_page():
    return "Welcome to the Home Page"

# run the app
if __name__ == '__main__':
    app.run(debug=True)