import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to deployment"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8001))
    app.run(host='0.0.0.0', port=port)
