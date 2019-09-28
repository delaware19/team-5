import sqlite3
from flask import Flask, render_template, request
import werkzeug
from flask import g

DATABASE = '/Users/ryan_emenheiser/Desktop/CodeForGood/team-5/c4gDataBase.db'
app = Flask(__name__)
connection = sqlite3.connect("c4gDataBase.db")
cursor = connection.cursor()


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

# for uploading an image from the admin's gallery
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(werkzeug.secure_filename(f.filename))
        return 'file uploaded successfully'


@app.route("/story", methods=["POST"])
def query_story():

    connection = sqlite3.connect("c4gDataBase.db")
    cursor = connection.cursor()
    name = request.form["Name"]
    age_group = request.form["Age Group"]
    gender = request.form["Gender"]
    treatment = request.form["Treatment"]


    sID = name + age_group[0]
    if gender.upper() == "MALE":
        sID += "0"
    elif gender.upper() == "FEMALE":
        sID += "1"
    else:
        sID += "2"
    response = cursor.execute("SELECT TEXT_CAPTIONS FROM Story, Text WHERE STORY.STORY_ID = \"%s\" AND TEXT.STORY_ID = \"%s\"" % (sID, sID))
    #connection.close()
    # todo querying the database via POST request
  

    # return render_template("storyResult.html", name = name, age_group = age_group, gender = gender, treatment = treatment, response = response.fetchall())
    return render_template("readStories.html", response = response.fetchall())

# Gain access to db
def get_database():
    database = getattr(Flask, '_database', None)
    if database is None:
        database = Flask._database = sqlite3.connect(DATABASE)

#Need to figure out img list for method signature ------------------->
def insertVaribleIntoTable(name, age, gender, story_ID, type_of_visit):
    try:
        sqliteConnection = sqlite3.connect('c4gDataBase.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = "INSERT INTO Story (NAME, AGE, GENDER, STORY_ID, TYPE_OF_VISIT, IMAGE_LIST), VALUES (\"%s\", \"%d\", \"%d\", \"%s\", \"%s\", \"%s\")" % (name, age, gender, story_ID, type_of_visit, img_list)

        data_tuple = (name, age, gender, story_ID, type_of_visit)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVaribleIntoTable('Joe', 15, 'Male', 'Joe150', "ER")


@app.teardown_appcontext
def close_database(exception):
    database = getattr(Flask, '_database', None)
    if database is not None:
        database.close()


if __name__ == "__main__":
    app.run(debug=True)
