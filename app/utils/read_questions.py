from __future__ import annotations

import xlrd

from app.utils.types import SingleQuestion, MultiQuestion

def read_questions(file: str) -> tuple[list[SingleQuestion], int, list[MultiQuestion], int]:
  data = xlrd.open_workbook(file)
  table = data.sheet_by_index(0)
  single: list[SingleQuestion] = []
  multi: list[MultiQuestion] = []

  for row in range(1, table.nrows):
    q = {}
    q['id'] = row
    q['type'] = table.cell_value(row, 0)
    q['content'] = table.cell_value(row, 1)
    q['choice'] = [{c[0]: c[2:].replace('；', '')} for c in table.cell_value(row, 2).split('\n')]
    q['answer'] = list(table.cell_value(row, 3))
    q['explanation'] = table.cell_value(row, 4)
    q['difficulty'] = table.cell_value(row, 5)

    if q['type'] == '单选题': single.append(q)
    if q['type'] == '多选题': multi.append(q)

  return single, len(single), multi, len(multi)