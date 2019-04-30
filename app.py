from flask import *

app = Flask(__name__)

app.secret_key = r"\G)cTBS.iX3]&r6{:e'v5XNksS}5E:D6CP"

@app.route("/")
def index():
    return render_template('index.html')

