from flask import Flask
from Controllers.views import *
application = Flask(__name__)


application.add_url_rule('/v/search_face','search_face',search_face, methods = ['POST'])

if __name__ == "__main__":
	application.run(host='0.0.0.0', port=3000)