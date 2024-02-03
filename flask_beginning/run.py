from flaskblog import app #when it s in the form of package it imports from __init__.py

print("""CHECK HERE FOR LOGIN: 
s@gmail.com, 
password = 'test'""")

if __name__ == '__main__':
    app.run(debug = True)


