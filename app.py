from flask import Flask
banana = Flask(__name__)

from controllers import controller
banana.run(debug=True)