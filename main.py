<<<<<<< HEAD
import sqlite3
from flask import Flask, render_template
from flask import g

DATABASE = '/Users/ryan_emenheiser/Desktop/CodeForGood/team-5/c4gDataBase.db'
app = Flask(__name__)


@app.route("/home")
def home():

    return render_template("home.html", title = "Home Page")


#Gain access to db
def get_database():
    database = getattr(g, '_database', None)
    if database is None:
        database = g._database = sqlite3.connect(DATABASE)


@app.teardown_appcontext
def close_database(*args, **kwargs):
    database = getattr(g, '_database', None)
    if database is not None:
        database.close()


if __name__ == "__main__":
    app.run()
=======
import sqlite3
from flask import Flask, render_template

DATABASE = '/Users/ryan_emenheiser/Desktop/CodeForGood/team-5/c4gDataBase.db'
app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html", title="Home Page")


@app.route("/create/stories")
def create_stories():
    return render_template("admin_create_story.html")  # todo possible html path for creating admin stories


@app.route("/view")
def view_stories():
    return render_template("view_stories.html")  # todo possible html path


# Gain access to db
def get_database():
    database = getattr(Flask, '_database', None)
    if database is None:
        database = Flask._database = sqlite3.connect(DATABASE)


@app.teardown_appcontext
def close_database(exception):
    database = getattr(Flask, '_database', None)
    if database is not None:
        database.close()


if __name__ == "__main__":
    app.run()
>>>>>>> 4ecaca27b2bb4b1421348ffdb49fdbaa8225308d
