## Learning Flask for web-app
 #- user management
 #- blog style website
 #- login + forgot pw
 #- options for just login ppl
 #- add in picture
 #- add new post
 #- look at other ppl's post
 #- update/ delete posts
 

## pip install flask
from flask import Flask

app = Flask(__name__) ##creating app variable and setting it to instance of flask class

@app.route("/") ## route decorator to tell us different pages
@app.route("/home") ## will act as another route to the same page
def home():
    return "<h1>Home Page!</h1>" ## wrapping in HTML H1 tags to make it a heading

## in terminal we need to navigate to the directory and type export FLASK_APP = flask.py, then flask run to get the port site 
## need to stop server with ctrl + c and rerun using flask run to pick up changes
## we can run run in debug mode to avoid having to restart server everytime
## export FLASK_DEBUG =1
## flask run

@app.route("/about") ## will create a route to an about page
def about():
    return "<h1>About Page!</h1>"

if __name__ == '__main__': ## running our app directly using python and avoid enviroment variables, only works if we run it directly
    app.run(debug=True)