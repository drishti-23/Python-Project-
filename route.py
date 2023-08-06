from flask import Blueprint, request, jsonify
from controllers import *
from middleware import*  

app_route = Blueprint('app', __name__) 

@app_route.route('/signup', methods=['POST'])
@validate_params(['username','password'])
@password_validation
def signup_route():
    try:
        result, status_code = signup()
        return jsonify({'message':result, 'status':status_code})
    except Exception as e:
        return jsonify({'message':'Internal Server Error', 'error': str(e), "status code": 500})

@app_route.route('/login', methods=['POST'])   
@validate_params(['username','password'])
@password_validation
def login_route():
    try:
        result, status_code = login()
        return jsonify(result), status_code 
    except Exception as e:
        return jsonify({'message': 'Internal SServer Error', 'error': str(e), "status code": 500})

@app_route.route('/home', methods=['GET'])
@jwt_required()
@protected_route
def home():
    try:
        result, status_code = home()
        return jsonify(result), status_code
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e), "status code": 500})
    
#app_auth.add_url_rule('/signup', view_func=signup, methods=['POST'])
#app_auth.add_url_rule('/login', view_func=login, methods=['POST'])
#app_auth.add_url_rule('/home', view_func=home, methods=['GET'])    