from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return 'Welcome to my first CICD  Application deployed on GKE '

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)