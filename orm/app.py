from flask import Flask, request
from database.database import session
from database.models import Person, Base

app = Flask(__name__)



@app.route("/user")
def query():
    args = dict(request.args)
    id = args["id"]
    firstname = args["firstname"]
    lastname = args["lastname"]
    gender = args["gender"]
    age = args["age"]
    person = Person(id=id,
                    firstname=firstname,
                    lastname=lastname,
                    gender=gender,
                    age=age)
    
    with session() as sess:
        
        sess.add(person)
        sess.commit()

    return "User has been added"


if __name__ == "__main__":
    app.run(debug=True)
