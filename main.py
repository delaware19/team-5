import sqlite3
from flask import Flask

DATABASE = '/path/to/database.db'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

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