import flask

app = flask.Flask(__name__, template_folder='./dist',static_folder='./assets')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login')
def login():
    return flask.render_template('login.html')

@app.route('/signup')
def signup():
    return flask.render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)