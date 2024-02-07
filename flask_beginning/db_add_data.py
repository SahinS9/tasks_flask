from flaskblog import app, db
from flaskblog.models import User, Post
import random

app.app_context().push()

posts = []
for i in range(1,35):
    title = f"Title {i}"
    content = f"Content {i} for the new {i}. post"
    user_id = random.choice([1,2,3])
    post = Post(title = title, content=content, user_id=user_id)
    posts.append(post)

db.session.add_all(posts)
db.session.commit()




#########  NOTES   #########  
## PAGINATION

#in terminal

# >>> posts = Post.query.paginate(page = 6, per_page = 2)
# >>> for page in posts.iter_pages():
# ...     print(page)
# ... 
# 1
# 2
# None
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# None
# 16
# 17

#None is for not showing all pages, some from begin., some from end. and mid.abs
