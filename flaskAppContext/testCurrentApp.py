from flask import Flask, current_app

app = Flask("Demo Flask App")

with app.app_context():    
    print(app is current_app) # False
    print(app is current_app._get_current_object()) # True
    
    print(type(current_app)) # <class 'werkzeug.local.LocalProxy'>
    print(type(current_app._get_current_object())) # <class 'flask.app.Flask'>
    