import sqlite3
from flask import Flask, render_template

DATABASE = '/path/to/database.db'
app = Flask(__name__)


@app.route("/home")
def home():

    return render_template("home.html", title = "Home Page")




#Gain access to db
def get_database():
    database = getattr(Flask, '_database', None)
    if database is None:
        database = Flask._database = sqlite3.connect(DATABASE)


@app.teardown_appcontext
def close_database():
    database = getattr(Flask, '_database', None)
    if database is not None:
        database.close()


if __name__ == "__main__":
    app.run()