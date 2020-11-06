from flask import Flask
from flaskupload.data import Articles
from flask_bootstrap import Bootstrap
from passlib.hash import sha256_crypt
from flask_bcrypt import Bcrypt
# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from wtforms import Form
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# init flask
app = Flask(__name__)
# init bootstrap
Bootstrap(app)
mysql = MySQL()
app.config['MYSQL_HOST']= '127.0.0.1'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB'] = 'pharmbase'
app.config['MYSQL_CURSORCLASS']='DictCursor'
app.config['SECRET_KEY'] = '45c7a07dc26848d5e138efe08d8a3db9'

# init mysqldb
# mysql=MySQL(app)
mysql.init_app(app)

# init login manager
login_manager=LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bcrypt =Bcrypt(app)

from flaskupload import routes