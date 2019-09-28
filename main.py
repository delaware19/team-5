import sqlite3
from flask import Flask, render_template, request
import werkzeug

from flask import g

DATABASE = '/Users/ryan_emenheiser/Desktop/CodeForGood/team-5/c4gDataBase.db'
app = Flask(__name__)

name = "Joe"
gender = "Female"

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


@app.route("/create/stories/success", methods=["POST"])
def adding_to_database():
    name = request.form.get("Name", "Joe")
    print(request.form)
    print("Gender:" + str(request.form.get("Gender")))
    if name is not None:
        story_id = makeStoryID(request.form.get("Name"), request.form.get("Age Group"), request.form.get("Gender"))
        insertVaribleIntoTable(request.form.get("Name"), request.form.get("Age Group"), request.form.get("Gender"), story_id,
                               request.form.get("Treatment"), request.form.get("image"))

        print("Database insert succeed")
    else:
        print("Gender:" + request.form["Gender"])
    return "Success"
# for uploading an image from the admin's gallery
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(werkzeug.secure_filename(f.filename))
        return 'file uploaded successfully'


@app.route("/story", methods=["POST"])
def query_story():
    # todo querying the database via POST request
    return render_template("storyResult.html", story='database_story')


def insertVaribleIntoTable(name, age, gender, story_ID, type_of_visit, img_list):
    try:
        sqliteConnection = sqlite3.connect("c4gDataBase.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = cursor.execute(
            "INSERT INTO Story(NAME, AGE, GENDER, STORY_ID, TYPE_OF_VISIT, IMAGE_LIST) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (
                name, age, gender, story_ID, type_of_visit, img_list))

        data_tuple = (name, age, gender, story_ID, type_of_visit, img_list)
        # cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()

        print("Python Variables inserted successfully into SqliteDb_developers table")
        return "Success"
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return ""


def makeStoryID(name, age, gender):
    sID = name + str(age)
    if gender.upper() == "MALE":
        sID += "0"
    elif gender.upper() == "FEMALE":
        sID += "1"
    else:
        sID += "2"

    return sID


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
    app.run(debug=True)
