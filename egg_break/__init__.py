from flask import Flask

my_app = Flask(__name__)

from egg_break import routes
