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

