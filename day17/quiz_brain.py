

class QuizBrain:   
    def __init__(self,q_list) -> None:
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
        self.end = False
    def check(self,answer_p,correct_p):
        if answer_p.lower() == correct_p.lower():
            self.score +=1
            print(f"Yoour score is {self.score}")
        else:
            print(f"Yoour score is {self.score}")
            print(f"You Lose")
            self.end = True

    def still_has_ques(self):
        return self.question_num < len(self.question_list)
           
    def next_ques(self):
        ques = self.question_list[self.question_num]
        self.question_num+=1
        
        user_answer = input(f"Q.{self.question_num}. {ques.text} True/False: ")
        correct = ques.ans
        self.check(user_answer,correct)


