
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for data in question_data:
   newobj = Question(data["text"],data["answer"])
   question_bank.append(newobj)
  

quiz = QuizBrain(question_bank)

while quiz.still_has_ques() and quiz.end == False:
    quiz.next_ques()
