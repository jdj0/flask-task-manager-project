import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# test message to see if all is working
@app.route("/")
def hello():
    return "Hello World... again again again!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)