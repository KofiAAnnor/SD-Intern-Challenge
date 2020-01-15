from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initializing app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interns.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
list_of_positions = ["Software Development Intern"]


# Declaring database model
class Intern(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    school = db.Column(db.String(80), nullable=False)
    degree_program = db.Column(db.String(80), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return jsonify({self.first_name, self.last_name, self.position, self.school, self.degree_program})


db.drop_all()
db.create_all()
db.session.commit()


# Validates intern positions
def positions_are_valid(interns):
    for intern in interns:
        if not list_of_positions.__contains__(intern["position"]):
            return False
    return True


#  Retrieves intern data
def get_intern_data():
    all_interns = Intern.query.all()
    all_interns_array = []
    for each_intern in all_interns:
        intern_dictionary = {
            "id": each_intern.id,
            "first_name": each_intern.first_name,
            "last_name": each_intern.last_name,
            "position": each_intern.position,
            "school": each_intern.school,
            "degree_program": each_intern.degree_program,
            "time of entry": each_intern.time,
        }
        all_interns_array.append(intern_dictionary)
    return jsonify(all_interns_array)


# Serves GET and POST requests for API
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not positions_are_valid(request.json):
            return "invalid position type\n", 400
        for x in request.json:
            first_name = x['first_name']
            last_name = x['last_name']
            position = x['position']
            school = x['school']
            degree_program = x['degree_program']
            intern = Intern(first_name=first_name, last_name=last_name, position=position, school=school,
                            degree_program=degree_program)
            db.session.add(intern)
            db.session.commit()
        return "request received\n", 200
    elif request.method == 'GET':
        return get_intern_data()
    else:
        return "invalid request\n", 400


# Running application
if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
