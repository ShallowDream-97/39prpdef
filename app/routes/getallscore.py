from flask import Blueprint, request, json

from app.utils.types import StudentAnswerRecord as StudentAnswerRecordT
from app.utils.database_schema import StudentAnswerRecord as StudentAnswerRecordS

getallscore = Blueprint('getallscore', __name__, url_prefix='/api')

@getallscore.route('/getallscore', methods=['GET'])
def index():
  answer_record: list[StudentAnswerRecordS] = StudentAnswerRecordS.objects(studentid=request.args.get('studentid'))
  if len(answer_record) == 0:
    res: StudentAnswerRecordT = {
      'studentid': request.args.get('studentid'),
      'record': []
    }
    return json.dumps(res, ensure_ascii=False)

  else:
    return answer_record[0].to_json()
