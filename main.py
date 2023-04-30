from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    blog = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/post/<blog_id>")
def get_blog(blog_id):
    post = Post(blog_id)
    return render_template("post.html", post=post.blog_post, blog_id=post.blog_id)

''' Method Before Class Implentation
def get_blog(blog_id):
    blog = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog)
    all_posts = response.json()
    for post in all_posts:
        if post["id"] == int(blog_id):
            blog_post = post
            break
    else:
        blog_post = None

    return render_template("post.html", post=blog_post, blog_id=blog_id)
'''

if __name__ == "__main__":
    app.run(debug=True)
