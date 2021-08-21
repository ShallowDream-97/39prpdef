from flask import Blueprint

alive = Blueprint('alive', __name__, url_prefix='/api')

@alive.route('/alive')
def index():
  return 'server is alive'