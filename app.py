from flask import Flask, render_template, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs361_marticad"
app.config["MYSQL_PASSWORD"] = "3455"
app.config["MYSQL_DB"] = "cs361_marticad"
db = MySQL(app)


def execute_query(query_string=None):
    if query_string is None or len(query_string.strip()) == 0:
        return "error: query empty"
    cursor = db.connection.cursor()
    cursor.execute(query_string)
    return str(cursor.fetchall())


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/user/<string:user_id>/")
def user(user_id):
    return f"This is the profile page for user {user_id}."


@app.route("/feed/")
def feed():
    return render_template("feed.html")

@app.route("/createpost/")
def createpost():
    return render_template("createpost.html")


@app.route("/create-new/", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")

    if request.method == "POST":
        user_ID = request.form["user_ID"]
        post_head = request.form["post_head"]
        post_body = request.form["post_body"]



app.run(host="localhost", port=5000, debug=True)
