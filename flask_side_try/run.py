from tasks_app import app
import os

print('test functions in this app, port is 7000')

# Set the port dynamically, defaulting to 6000 if not provided
port = int(os.environ.get('PORT', 7000))

if __name__ == '__main__':
    app.run(port=port, debug=True)



