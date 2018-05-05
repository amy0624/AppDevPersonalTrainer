from flask import jsonify
from flask import request
from todo import app
from todo import Db as db
import json
from todo import models
from models import Model


@app.route('/users', methods=['POST'])
def post_tasks():
    Name = request.args.get("Name")
    Height = int(request.args.get("Height"))
    Weight = int(request.args.get("Weight"))
    Age = int(request.args.get("Age"))
    Gender = request.args.get("Gender")
    #Fitness_Level = int(request.args.get("Fitness_Level"))
    #Intensity = int(request.args.get("Intensity"))

    user = models.User(Name, Height, Weight, Age, Gender)

    user_dict = user.to_dict()
    db.add_user(user_dict["Name"], user_dict["Height"], user_dict["Weight"], user_dict["Age"],
    user_dict["Gender"])

    return jsonify(user_dict)

@app.route('/users', methods=['GET'])
def get_users_name():
    return jsonify(db.get_user_info_by_name(request.args.get("Name")))

@app.route('/users', methods=['DELETE'])
def delete_task():
    return jsonify(db.delete_user(request.args.get("Name")))

@app.route('/routines', methods=['GET'])
def get_all_routines():
    db.set_up_routines()
    return jsonify(db.get_list_of_routines())