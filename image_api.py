from flask import send_file
from flask import Flask, render_template, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


@app.route('/get_image')
def get_image():
    filename = "/home/syam/Downloads/welcome.jpeg"    
    return send_file(filename, mimetype='image/jpeg')


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6767, debug=True, threaded=True)