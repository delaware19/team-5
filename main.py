import sqlite3
from flask import Flask, render_template, request
from flask import g
import sqlite3

DATABASE = '/Users/ryan_emenheiser/Desktop/CodeForGood/team-5/c4gDataBase.db'
app = Flask(__name__)
connection = sqlite3.connect("c4gDataBase.db")
cursor = connection.cursor()

# sql_command = """
# SELECT *
# FROM Story, Text WHERE STORY.STORY_ID = "Ryan210";
# """
# response = cursor.execute(sql_command)
# print(response)
# connection.close()


@app.route("/")
def home():
    return render_template("home.html", title="Home Page")


@app.route("/create/stories", methods=["POST"])
def create_stories():
    return render_template("createStories.html")  # todo possible html path for creating admin stories


@app.route("/login")
def login():
    return render_template("login.html", login="login")


@app.route("/find")
def find_stories():
    return render_template("findStories.html")


@app.route("/read")
def read_stories():
    return render_template("readStories.html")


@app.route("/story", methods=["POST"])
def query_story():

    connection = sqlite3.connect("c4gDataBase.db")
    cursor = connection.cursor()

    sql_command = """
    SELECT *
    FROM Story, Text WHERE STORY.STORY_ID = "Ryan40";
    """
    response = cursor.execute(sql_command)
    #connection.close()
    # todo querying the database via POST request
    name = request.form["Name"]
    age_group = request.form["Age Group"]
    gender = request.form["Gender"]
    treatment = request.form["Treatment"]

    return render_template("storyResult.html", name = name, age_group = age_group, gender = gender, treatment = treatment, response = response.fetchall())


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
