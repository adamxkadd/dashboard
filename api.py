from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about')
def about():
    return 'About'
  
@app.route('/', methods =['GET', 'POST'] )
def home():
	my_data = {'text' : 'texte', 'int' : 123, 'message' : 'Hello, Flask!'}
	return jsonify(my_data)
