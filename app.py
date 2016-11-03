from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/')

@app.route('/index')
def root():
    return app.send_static_file('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9030)



