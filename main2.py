import sqlite3
from flask import Flask, render_template, request, url_for
import werkzeug
from flask import g

DATABASE = '/Users/ryan_emenheiser/Desktop/CodeForGood/team-5/c4gDataBase.db'
app = Flask(__name__)
connection = sqlite3.connect("c4gDataBase.db")
cursor = connection.cursor()

#possible issue if the split string does not exist will not work
#  however, if these are the functions used should not be an issue

#takes in the the string of TEXT_CAPTIONS and will turn it into an array
#  that can be traversed for each of the story "pages" to put the correct
#  text per story "page"
def parseText(textStr):
    textArr = textStr.split("###")
    
    return textArr

#takes in the array of TEXT_CAPTIONS and will turn it into a string that
#  is saved into the database, and is parsed by parseText
def translateText(textArr):
    textStr = ""
    for i in range(len(textArr)):
        textStr += str(textArr[i]) + "###"
        
    return textStr

#takes in the the string of IMAGE_LIST and will turn it into an array
#  that can be traversed for each of the story "pages" to put the correct
#  image per story "page"
def parseImage(imageStr):
    imageArr = imageStr.split(", ")
    
    return imageArr

#takes in the array of IMAGE_LIST and will turn it into a string that
#  is saved into the database, and is parsed by parseImage
def translateImage(imageArr):
    imageStr = ""
    for i in range(len(imageArr)):
        if i == len(imageArr) - 1:
            imageStr += imageArr[i]
        else:
            imageStr += imageArr[i] + ", "
        
    return imageStr

print(parseText("this is caption 1 ### this is caption 2 ###"))
print(translateText(['this is caption 1', 'this is caption 2']))

print(parseImage("test1, test2"))
print(translateImage(['test1', 'test2']))


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
   # image = request.form["Image"]

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
    response = response.fetchall()
    result = parseText(response[0][0])
    # return render_template("storyResult.html", name = name, age_group = age_group, gender = gender, treatment = treatment, response = response.fetchall())
    return render_template("readStories.html", response = result)

# Gain access to db
def get_database():
    database = getattr(Flask, '_database', None)
    if database is None:
        database = Flask._database = sqlite3.connect(DATABASE)

#Need to figure out img list for method signature ------------------->

def insertVaribleIntoTable(name, age, gender, story_ID, type_of_visit, img_list):
    try:
        sqliteConnection = sqlite3.connect("c4gDataBase.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = cursor.execute("INSERT INTO Story(NAME, AGE, GENDER, STORY_ID, TYPE_OF_VISIT, IMAGE_LIST) VALUES (\"%s\", \"%d\", \"%s\", \"%s\", \"%s\", \"%s\");" % (name, age, gender, story_ID, type_of_visit, img_list))

        data_tuple = (name, age, gender, story_ID, type_of_visit, img_list)
        #cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

    return render_template("home.html")

#insertVaribleIntoTable('Joe', 15, 'Male', 'Joe150', "ER", ["test"])


@app.teardown_appcontext
def close_database(exception):
    database = getattr(Flask, '_database', None)
    if database is not None:
        database.close()

@app.teardown_request
def teardown_request(exception=None):
    print("this runs after request")

def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')

if __name__ == "__main__":
    app.run(debug=True)



