from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    name = "World"
    return render_template('index.html',name=name)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
