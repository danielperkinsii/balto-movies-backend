from flask import Flask, g
from flask_cors import CORS

import models
from resources.movies import movie # adding this line


DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

CORS(movie, origins=['http://localhost:3000'], supports_credentials=True) 

app.register_blueprint(movie, url_prefix='/movies')

@app.route('/hi')
def index():
    return 'hello, world'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)