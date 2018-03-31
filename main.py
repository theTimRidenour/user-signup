from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    return render_template("sign-up.html")

@app.route("/", methods=["POST"])
def validate():
    name = request.form['username']
    pw = request.form['pw']
    verify_pw = request.form['verify_pw']
    email = request.form['email']

    if (name == "" or len(name) < 3 or len(name) > 20 or " " in name or name[0].isdigit() or name[0].isalnum() == False):
        return render_template("sign-up.html", error="Username must be between 3 and 20 characters, start with a letter, and cannot contain spaces.", error_type = 1, email=email)

    if (pw == "" or len(pw) < 8 or len(pw) > 20 or any(x.isupper() for x in pw) == False or any(x.islower() for x in pw) == False or any(x.isdigit() for x in pw) == False or pw[0].isdigit() or pw[0].isalnum() == False):
        return render_template("sign-up.html", error="Password must be between 8 and 20 characters, start with a letter, and contain a capital letter, a lower case letter, and a number.", error_type = 2, username=name, email=email)

    if (verify_pw == ""):
        return render_template("sign-up.html", error="You must verify your password.", error_type = 3, username=name, email=email)

    if (pw != verify_pw):
        return render_template("sign-up.html", error="Your passwords do not match.", error_type = 3, username=name, email=email)

    if (email != ""):
        at_cnt = 0
        period_cnt = 0
        for x in email:
            if (x == "@"):
                at_cnt += 1
            if (x == "."):
                period_cnt += 1
        if (at_cnt != 1 or period_cnt != 1 or " " in email or len(email) < 3 or len(email) > 20):
            return render_template("sign-up.html", error="You did not enter a valid email address. ex: you@place.com", error_type = 4, username=name)

    return render_template("welcome.html", username = name, title = "Welcome, " + name + "!")

app.run()
