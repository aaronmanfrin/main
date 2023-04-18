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
from flask import Flask, render_template, url_for

posts = [ ## adding in dummy blog posts as a list of dictionaries
    {
        'author':"Aaron",
        'title':'Blog Post 1',
        'content': 'First post test',
        'date_posted':' April 17 2023'
    },
    {
        'author':"Languine",
        'title':'Cat Post 1',
        'content': 'First cat post test',
        'date_posted':' April 18 2023'
    }
]
app = Flask(__name__) ##creating app variable and setting it to instance of flask class

@app.route("/") ## route decorator to tell us different pages
@app.route("/home") ## will act as another route to the same page
def home():
    return render_template('home.html',posts=posts) ## telling it to render file from templates folder, and passing in the posts as a variable that can be used in the html (it will be the left side of the =)

##in terminal we need to navigate to the directory and type export FLASK_APP = flask_l.py, then flask run to get the port site 
## need to stop server with ctrl + c and rerun using flask run to pick up changes
## we can run run in debug mode to avoid having to restart server everytime
## export FLASK_DEBUG =1
## flask run

@app.route("/about") ## will create a route to an about page
def about():
    return render_template('about.html',title='About') ## adding a title to be passed into the title section of html

if __name__ == '__main__': ## running our app directly using python and avoid enviroment variables, only works if we run it directly
    app.run(debug=True)



## create a templates folder to store the html files and css files