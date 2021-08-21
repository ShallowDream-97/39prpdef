from flask import Blueprint, json

from app.utils.types import RankingEntry, AnswerRecord
from app.utils.database_schema import StudentAnswerRecord

getranking = Blueprint('getranking', __name__, url_prefix='/api')

@getranking.route('/getranking', methods=['GET'])
def index():
  all_rec: list[StudentAnswerRecord] = StudentAnswerRecord.objects()
  ranking: list[RankingEntry] = []
  for rec in all_rec:
    stuid: str = rec.studentid
    scores: list[AnswerRecord] = [{'time': s.time, 'score': s.score} for s in rec.record]
    hs: AnswerRecord = sorted(scores, key=lambda s: s['score'], reverse=True)[0]
    ranking.append({'studentid': stuid, 'highscore': hs})

  return json.dumps(sorted(ranking, key=lambda r: r['highscore']['score'], reverse=True), ensure_ascii=False)