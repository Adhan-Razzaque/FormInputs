from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    animal = request.form.get('input_animal', '')
    personality = request.form.get('input_personality', '')
    extrainfo = request.form.get('input_extrainfo', '')
    letter = request.form.get('input_freeform', '')
    gryffindor = 0
    slytherin = 0
    hufflepuff = 0
    ravenclaw = 0
    if animal is "Lion":
        gryffindor += 1
    elif animal="Raven":
        ravenclaw += 1
    elif animal="Snake":
        slytherin += 1
    elif animal="Badger":
        hufflepuff += 1
    if personality="Bravery":
        gryffindor += 1
    elif personality="Wisdom":
        ravenclaw += 1
    elif personality="Ambition":
        slytherin += 1
    elif personality="Loyalty":
        hufflepuff += 1
    if "Honest" in extrainfo:
        gryffindor += 1
    elif "Idealistic" in extrainfo:
        gryffindor += 1
    ##elif "Driven" in extrainfo:
    ##    gryffindor += 1
    ##elif "Independant" in extrainfo:


    return render_template("main_page.html",
                           intro="You're a wizard %s." % name,
                           body="It looks like you're a %s." % house,
                           outro="Your letter has been sent to Hogwarts")

#Login Page Pseudo-Code
#POST Username, Password if login is present
#If not present, POST Username, Password, and E-Mail. Do a Client-Side Verification for password
#Use attributes in the html to hide password and make more accessible for screen readers