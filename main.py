from flask import Flask
import os

app = Flask(__name__)
port = (os.environ.get("PORT", 9001))

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, port=port, host="0.0.0.0")
