from models.post import  Post
from database import  Database
from menu import Menu
from models.blog import Blog

Database.initialize()

#
# post = Post(blog_id="000",
#             title="Festival",
#             content="Some event had been organige",
#             author='Annn)
#
# post.save_to_mongo()
post=Post.from_mongo('99e2aba86def4873a0325c5f27f7b61d')
print(post)
#
# blog  = Blog(author="jose",
#              title="Simple title",
#              description="sample description")
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts())
#
# menu = Menu()
# menu.run_menu()
