from models.post import  Post
from database import  Database
from menu import Menu
from models.blog import Blog

Database.initialize()


post = Post(blog_id="000",
            title="Festival",
            content="Some event had been organige",
            author='Annn')

post.save_to_mongo()


print(post)

posts=Post.from_blog("123")

for post in posts:
    print(post)

