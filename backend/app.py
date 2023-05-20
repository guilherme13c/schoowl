from flask import Flask, session, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>test</p>"

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session['username'] == request.form['username']
        return redirect(url_for('index'))
    return """
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """
