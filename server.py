from flask import Flask
from mongoengine import connect

from app.routes import alive, getquestions, sendanswers, register, getallscore, getranking

app = Flask(__name__)

app.register_blueprint(alive)
app.register_blueprint(getquestions)
app.register_blueprint(sendanswers)
app.register_blueprint(register)
app.register_blueprint(getallscore)
app.register_blueprint(getranking)

if __name__ == '__main__':
  connect(host='mongodb://admin:admin@localhost:27017/app_dev_proj')
  app.run(debug=True)