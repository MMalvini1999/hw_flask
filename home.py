from flask import Flask
from flask import escape

myapp_obj = Flask(__name__)

@myapp_obj.route("/home")
def home():
	return "Home Page"
myapp_obj.run()

