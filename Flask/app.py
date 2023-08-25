from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import pandas as pd
import random

database = pd.read_csv('database.csv')

Login = False
name = ""

app = Flask(__name__)

# Load the trained model
model = load_model('../my_model.h5')

# Define class labels
class_labels = ['Ahmedabad', 'Delhi', 'Kerala', 'Kolkata', 'Mumbai']

# Set the threshold for minimum accuracy
threshold = 0.5

# Create a function to process the uploaded image
def process_image(uploaded_file):
    img = Image.open(uploaded_file)
    img = img.resize((150, 150))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
    accuracy = predictions[0][predicted_class_index]


    if all(accuracy < threshold for accuracy in predictions[0]):
        return "This location is not in our database. Please try again with a different image."
    else:
        result = f"City: {predicted_class_label},&nbsp;&nbsp;Accuracy: {accuracy*100:.02f}%"

        return result

@app.route("/play", methods=["GET", "POST"])
def index():
    if request.method == "POST" and Login == True:
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            result = process_image(uploaded_file)
            return render_template("indexLS.html",name = name, result=result)
    elif Login:
        return render_template("indexLS.html", name=name)
    else:
        result = "Please login to continue"
        return render_template("index.html",result=result)


@app.route("/")
def home():
    if Login:
        return render_template("HomeLS.html", name=name)
    return render_template("Home.html")

@app.route("/play")
def play():
    return render_template("index.html")

@app.route("/loginprc",methods=["GET", "POST"])
def loginprc():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pass")
        if username in database['username'].values:
            result = database[database['username'] == username]
            if password in result['password'].values:
                global Login
                Login = True
                global name
                name = username
                return render_template("HomeLS.html", name=name)
            else:
                result = "Incorrect Password"
                return render_template("login.html",result=result)
        else:
            resultu = "Incorrect Username or user does not exist"
            return render_template("login.html",result=resultu)

    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signupprc",methods=["GET", "POST"])
def signupprc():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password1")
        conf_password = request.form.get("password2")
        email = request.form.get("email")
        if username == "" or password == "" or conf_password == "" or email == "":
            result = "Please fill all the fields"
            return render_template("signup.html",result=result)
        if username in database['username'].values:
            result = "Username already exists"
            return render_template("signup.html",result=result)
        elif password != conf_password:
            result = "Passwords do not match"
            return render_template("signup.html",result=result)
        else:
            database.loc[len(database.index)] = [username,email,password]
            database.to_csv('database.csv',index=False)
            global Login
            Login = True
            global name
            name = username
            return render_template("HomeLS.html", name=name)
    return render_template("signup.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
