from flask import redirect, render_template, url_for, request, session, flash
from app.models.source import source
from app import app, db
from app.insert.insert_file import upload_file

# app = Flask(__name__)
app.secret_key = "hello"


@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/file", methods=["POST", "GET"])
def file():
    if request.method == "POST":
        upload_file()
        return redirect(url_for("home"))
    else:
        if session.permanent:
            return render_template("upload.html")
        return render_template("upload.html")

@app.route("/data")
def data():
    if session.permanent:
        table_data = source.query.all()
        return render_template("data.html", table_data=table_data)
    else:
        return redirect(url_for("file"))


@app.route("/delete")
def delete():
    if session.permanent:
        db.session.query(source).delete()
        db.session.commit()
        session.permanent = False
        flash("Data has been deleted", "info")
    else:
        flash("Upload the CSV file first", "info")
    return redirect(url_for("home"))

def configure():
    source()

configure()

if __name__ == "__main__":
    app.run(debug=True)