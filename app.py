from flask import Flask
from  models import db 
from middleware import jwt
from route import app_route

def create_app():
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   app.config['JWT_SECRET_KEY'] = 'BIHUJFegdsal'  # Change this to your preferred secret key

   db.init_app(app)
   jwt.init_app(app)
   app.register_blueprint(app_route, url_prefix='/')

   with app.app_context():
      db.create_all()

   return app

app=create_app()
if __name__ == '__main__':
   app.run(debug=True)