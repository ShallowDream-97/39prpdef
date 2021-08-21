import mongoengine
from datetime import datetime

from mongoengine.fields import EmbeddedDocumentField

class QuestionRecord(mongoengine.Document):
  sessionid = mongoengine.StringField(required=True)
  studentid = mongoengine.StringField(required=True)
  questionid = mongoengine.ListField(mongoengine.IntField(), required=True)

class AnswerRecord(mongoengine.EmbeddedDocument):
  time = mongoengine.StringField(required=True)
  score = mongoengine.IntField(required=True)

class StudentAnswerRecord(mongoengine.Document):
  studentid = mongoengine.StringField(required=True)
  record = mongoengine.ListField(EmbeddedDocumentField(AnswerRecord), required=True)

class Student(mongoengine.Document):
  wxname = mongoengine.StringField(required=True)
  studentid = mongoengine.StringField(required=True)