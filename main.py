from flask import Flask, render_template
import requests
BLOG_ENDPOINT='https://api.npoint.io/9dd7cb66e29c10f32d83'
app = Flask(__name__)
response = requests.get(BLOG_ENDPOINT)
blogs = response.json()
@app.route('/')
def home():
    return render_template("index.html",blogs=blogs)
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:index>')
def show_post(index):
    requested_post=None
    for blog in blogs:
        print(blog)
        if blog['id']==index:
            requested_post=blog
    return render_template('post.html',post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
