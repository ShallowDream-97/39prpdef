from flask import Blueprint, request, json
from datetime import datetime

from app.utils.read_questions import read_questions
from app.utils.types import AnswerReq, AnswerRes
from app.utils.database_schema import QuestionRecord, AnswerRecord, StudentAnswerRecord

sendanswers = Blueprint('sendanswers', __name__, url_prefix='/api')

@sendanswers.route('/sendanswers', methods=['POST'])
def index():
  single_q, num_single_q, multi_q, num_multi_q = read_questions('./app/utils/question_excel.xls')
  received: AnswerReq = request.get_json()
  # get corresponding session from database
  session: QuestionRecord = QuestionRecord.objects(sessionid=received['sessionid'])[0]

  score = 0
  right_ids = []
  wrong_ids = []
  for i in range(len(received['answers'])):
    ans = list(received['answers'][i])
    ans.sort()
    db_ans = [q for q in single_q + multi_q if q['id'] == session.questionid[i]][0]['answer']
    db_ans.sort()
    if ans == db_ans:
      score += 1
      right_ids.append(session.questionid[i])

    else: wrong_ids.append(session.questionid[i])
  
  res: AnswerRes = {
    'score':score
  }

  # database stuff
  record = AnswerRecord(score=score, time=datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
  student_record: list[StudentAnswerRecord] = StudentAnswerRecord.objects(studentid=session.studentid)
  if len(student_record) == 0:
    student_record: StudentAnswerRecord = StudentAnswerRecord(studentid=session.studentid, record=[record])

  else:
    student_record: StudentAnswerRecord = student_record[0]
    student_record.record.append(record)

  student_record.save()

  # remove old session
  session.delete()

  return json.dumps(res, ensure_ascii=False)