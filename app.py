from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html")

@app.route("/photosessions")
def photosessions():
    return render_template("photosessions.html")

@app.route("/lookbooks")
def lookbooks():
    return render_template("lookbooks.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/reference")
def reference():
    return render_template("reference.html")

@app.route("/gods")
def gods():
    return render_template("gods.html")

@app.route("/citys")
def citys():
    return render_template("citys.html")

if __name__ == "__main__":
    app.run(debug=True)