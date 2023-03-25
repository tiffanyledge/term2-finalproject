from flask import Flask, redirect, render_template, request, url_for
import requests
import database_pratice as db

app = Flask(__name__)
api_key = '8e6bcea38d244f3a9d0c276030645072'

@app.route('/')
def index():

    return render_template('index.html' , data = db.get_api())


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    users = db.get_all_users()
    # print(users)

    #get the last user entered
    new_user = users.pop()

    all_data = {
        "user": new_user,
        "stock-data": db.get_api()
    }
    return render_template('home.html', data=all_data)

@app.route('/login_user' , methods=['POST'])
def login_user():

    password = request.form['password']

    data = {}
    user = db.validate_user (password)

    if user:
       
        data = {
            "name": user["name"],
        }

        #load home if there is a user, along with data.
        return render_template('home.html', data=data)
         

    else: 
        error_msg = "Login failed"

        data = {
            "error_msg": error_msg
        }
        #no user redirects back to the main login page, with error msg.
        return render_template('index.html', data=data)



@app.route('/post_user' , methods=['POST'])
def post_user():
    name = request.form['name']
    pw = request.form['password']
    
    db.store_user(name, pw)


    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



