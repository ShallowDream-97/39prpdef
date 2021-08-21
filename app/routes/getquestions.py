from flask import Blueprint, request, json
import random
import uuid

from app.utils.read_questions import read_questions
from app.utils.types import Question, QuestionRes
from app.utils.database_schema import QuestionRecord

getquestions = Blueprint('getquestions', __name__, url_prefix='/api')

@getquestions.route('/getquestions', methods=['GET'])
def index():
  single_q, num_single_q, multi_q, num_multi_q = read_questions('./app/utils/question_excel.xls')

  # prepare questions
  res_q: list[Question] = []
  if request.args.get('type') == 'single':
    res_q = random.sample(single_q, int(request.args.get('num')))
  elif request.args.get('type') == 'multi':
    res_q = random.sample(multi_q, int(request.args.get('num')))
  else:
    res_q = random.sample(single_q +multi_q, int(request.args.get('num')))

  res_q = [{
    'id': q['id'],
    'content': q['content'],
    'choice': [c for c in q['choice']],
    'difficulty': q['difficulty']
  } for q in res_q]

  # response object to client
  res: QuestionRes = {
    'sessionid': str(uuid.uuid4()),
    'questions': res_q
  }

  # save current answering session to database for future validation
  # question_record = QuestionRecord(questionid=res['questionid'], user=request.args.get('user'), contents=[r['content'] for r in res['questions']])
  # question_record.save()
  question_record: list[QuestionRecord] = QuestionRecord.objects(studentid=request.args.get('studentid'))
  if len(question_record) == 0:
    question_record: QuestionRecord = QuestionRecord(sessionid=res['sessionid'], studentid=request.args.get('studentid'), questionid=[r['id'] for r in res['questions']])
  
  else: # duplicate session: update to the latest
    question_record: QuestionRecord = question_record[0]
    question_record.sessionid = res['sessionid']
    question_record.questionid = [r['id'] for r in res['questions']]

  question_record.save()

  return json.dumps(res, ensure_ascii=False)