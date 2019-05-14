from flask import Flask, render_template, request
from models import UserModel
app = Flask(__name__)

@app.route("/login")
def hello():
    return render_template("login.html")


@app.route("/send",methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        kid= request.form['KID']
        ln= request.form['LastName']
        pas= request.form['Password']
        cf= request.form['ConfirmPassword']
        print(kid,ln,pas,cf)
        #connect to the database and get
        return kid
    return render_template('register.html')
if __name__ == "__main__":
    app.run(debug=True)