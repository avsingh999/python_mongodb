from models.post import  Post
from database import  Database
from menu import Menu
from models.blog import Blog

Database.initialize()

blog  = Blog(author="my_BLog",
             title="Simple blog title",
             description="sample blog description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())