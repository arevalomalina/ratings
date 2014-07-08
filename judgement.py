from flask import Flask, render_template, redirect, request
import model
app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    print user_list
    return render_template("user_list.html", users=user_list)

@app.route("/login")
def login():
    print "login"
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def process_login():
    """TODO: Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""
    print "check login"
    email = request.form["email"]
    print request.form
    #print email
    # 1) check if user exists (and has correct pwd)

    # 2) if user doesn't exist, create a user

    # 3) return some template or re-route
    return render_template("login.html")
    

@app.route("/create_new_user", methods=['POST'])
def create_new_user():
    pass


if __name__ == "__main__":
    app.run(debug = True)