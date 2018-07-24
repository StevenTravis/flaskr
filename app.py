from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/test')
def test_page():
	return 'hello test world'

@app.route('/index')
def index():
	user = {'username': 'Steven'}
	return render_template('index.html', title='Home', user = user)

if __name__ == '__main__':
	app.run()
