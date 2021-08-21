from __future__ import annotations

from typing import TypedDict

class SingleQuestion(TypedDict):
  id: int
  type: str
  content: str
  choice: list[dict[str, str]]
  answer: list[str]
  explanation: str
  difficulty: str

class MultiQuestion(TypedDict):
  id: int
  type: str
  content: str
  choice: list[dict[str, str]]
  answer: list[str]
  explanation: str
  difficulty: str

class Question(TypedDict):
  id: int
  difficulty: str
  content: str
  choice: list[dict[str, str]]

class QuestionRes(TypedDict):
  sessionid: str
  questions: list[Question]

class AnswerReq(TypedDict):
  sessionid: str
  answers: list[str]

class AnswerRes(TypedDict):
  score: int

class Student(TypedDict):
  wxname: str
  studentid: str

class AnswerRecord(TypedDict):
  time: str
  score: int

class StudentAnswerRecord(TypedDict):
  studentid: str
  record: list[AnswerRecord]

class RankingEntry(TypedDict):
  studentid: str
  highscore: AnswerRecord