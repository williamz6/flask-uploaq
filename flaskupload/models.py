from flaskupload import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  username = db.Column(db.String(100), unique=True, nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)



  def __repr__(self):
    return f"User('{self.username}', {self.email})"
  
  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return True
  
  def get_id(self):
    return str(self.id)


