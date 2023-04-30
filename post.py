import requests

class Post:
    def __init__(self, blog_id):
        self.blog_id = blog_id
        self.blog = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.blog)
        self.all_posts = self.response.json()
        self.blog_post = self._get_blog_post()

    def _get_blog_post(self):
        for post in self.all_posts:
            if post["id"] == int(self.blog_id):
                return post
        return None
