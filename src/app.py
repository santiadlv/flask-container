from flask import Flask, render_template, url_for, request, flash, redirect


app = Flask(__name__)
app.secret_key = "71f6af8da2fd66160ac6aa6a013a6106baedb5ec6de3f762e74b10cd1d5ad05a"


@app.route('/', methods=["GET"])
def root():
    return redirect(url_for("login"))
    
@app.route('/index', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        flag_usr = username[0].isupper()
        flag_pwd = password.isalnum() and not password.isalpha() and not password.isdigit()
        
        if flag_usr and flag_pwd:
            return redirect(url_for("index"))
        else:
            flash(
                message="Error: invalid username or password, please try again.",
                category="error"
            )
            return redirect(url_for('login'))
    else:
        return render_template("login.html")
