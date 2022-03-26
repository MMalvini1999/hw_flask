from flask import Flask, render_template
from flask import escape

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
	name="Lisa"
	city_names=['Paris', 'London', 'Rome', 'Tahiti']
	return f"""
        <h1>Welcome {name}!</h1>
        <a href="https://www.google.com">not google</a>

        <ul>
                <li>{city_names[0]}</li>
                <li>{city_names[1]}</li>
                <li>{city_names[2]}</li>
                <li>{city_names[3]}</li>
        </ul>"""
#myapp_obj.run()
