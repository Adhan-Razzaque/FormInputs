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
    extrainfo = request.form.getlist('extrainfo')
    letter = request.form.get('input_freeform', '')
    house = {'Gryffindor': 0, 'Slytherin': 0, 'Hufflepuff': 0, 'Ravenclaw': 0}
    if animal is "Lion":
        house['Gryffindor'] += 1
    elif animal is "Eagle":
        house['Ravenclaw'] += 1
    elif animal is "Snake":
        house['Slytherin'] += 1
    elif animal is "Badger":
        house['Hufflepuff'] += 1

    if personality is "Bravery":
        house['Gryffindor'] += 1
    elif personality is "Wisdom":
        house['Ravenclaw'] += 1
    elif personality is "Ambition":
        house['Slytherin'] += 1
    elif personality is "Loyalty":
        house['Hufflepuff'] += 1

    if "Honest" in extrainfo:
        house['Gryffindor'] += 1
    elif "Idealistic" in extrainfo:
        house['Gryffindor'] += 1
    elif "Driven" in extrainfo:
        house['Slytherin'] += 1
    elif "Intelligent" in extrainfo:
        house['Ravenclaw'] += 1
    elif "Determined" in extrainfo:
        house['Hufflepuff'] += 1
    elif "Patient" in extrainfo:
        house['Hufflepuff'] += 1
    elif "Charming" in extrainfo:
        house['Slytherin'] += 1
    elif "Inquisitive" in extrainfo:
        house['Ravenclaw'] += 1
    elif "Courageous" in extrainfo:
        house['Gryffindor'] += 1
    elif "Creative" in extrainfo:
        house['Ravenclaw'] += 1
    elif "Fair" in extrainfo:
        house['Hufflepuff'] += 1
    elif "Prideful" in extrainfo:
        house['Slytherin'] += 1

    ##elif "Driven" in extrainfo:
    ##    gryffindor += 1
    ##elif "Independant" in extrainfo:


    return render_template("main_page.html",
                           intro="You're a wizard %s." % name,
                           body="You are a likely a %s." % max(house, key=house.get),
                           outro="The following has been sent to the Sorting Hat for further review:\n %s" % letter)

#Login Page Pseudo-Code
#POST Username, Password if login is present
#If not present, POST Username, Password, and E-Mail. Do a Client-Side Verification for password
#Use attributes in the html to hide password and make more accessible for screen readers