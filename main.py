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
    if(name != "" and len(name) > 2 and len(name) < 21 and " " not in name and name[0].isdigit() == False and name[0].isalnum() == True):
        if(pw != "" and len(pw) > 7 and len(pw) < 21 and any(x.isupper() for x in pw) and any(x.islower() for x in pw) and any(x.isdigit() for x in pw) and pw[0].isdigit() == False and pw[0].isalnum() == True):
            if(verify_pw != ""):
                if(pw == verify_pw):
                    return render_template("sign-up.html", it="works")
                else:
                    return render_template("sign-up.html", error="Your passwords do not match.", error_type = 3, username=name, email=email)
            else:
                return render_template("sign-up.html", error="You must verify your password.", error_type = 3, username=name, email=email)
        else:
            return render_template("sign-up.html", error="Password must be between 8 and 20 characters, start with a letter, and contain a capital letter, a lower case letter, and a number.", error_type = 2, username=name, email=email)
    else:
        return render_template("sign-up.html", error="Username must be between 3 and 20 characters, start with a letter, and cannot contain spaces.", error_type = 1, email=email)

app.run()
