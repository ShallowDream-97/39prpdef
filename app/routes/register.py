from flask import Blueprint, request, json

from app.utils.types import Student as StudentT
from app.utils.database_schema import Student as StudentS

register = Blueprint('register', __name__, url_prefix='/api')

@register.route('/register', methods=['POST'])
def index():
  student: StudentT = {}
  # TODO: save student['wxname'] and student['studentid']
  # these two variables will be in "wxname" and "studentid" in the POST request,
  # so something like "/api/register?wxname=cwt&studentid=518030910031"
  student['wxname'] = request.args.get('wxname')
  student['studentid'] = request.args.get('studentid')

  student_record: list[StudentS] = StudentS.objects(studentid=student['studentid'])
  if len(student_record) == 0:
    student_record: StudentS = StudentS(wxname=student['wxname'], studentid=student['studentid'])

  else: # maybe something has changed
    student_record: StudentS = student_record[0]
    student_record.wxname = student['wxname']
    student_record.studentid = student['studentid']

  student_record.save()

  return 'success'