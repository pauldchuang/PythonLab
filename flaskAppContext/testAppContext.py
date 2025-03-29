from flask import Flask, current_app
from threading import Timer

app = Flask(__name__)

def background_task(passed_app):    
    with passed_app.app_context():
        print(passed_app.name)  # This will raise a RuntimeError

@app.route("/")
def index():
    Timer(1, background_task, args=[current_app._get_current_object()]).start()
    return "Task started!"

if __name__ == "__main__":
    app.run(debug=True)