from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return tandem.send_static_file('index.html')

@app.route("/time")
def time():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=8000)
