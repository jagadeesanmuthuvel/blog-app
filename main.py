from flask import Flask, render_template
import requests
BLOG_ENDPOINT='https://api.npoint.io/9dd7cb66e29c10f32d83'

app = Flask(__name__)

@app.route('/')
def home():
    response=requests.get(BLOG_ENDPOINT)
    blogs=response.json()
    return render_template("index.html",blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
