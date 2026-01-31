from flask import Blueprint
from flask_login import login_required, current_user

main = Blueprint('main', __name__)
