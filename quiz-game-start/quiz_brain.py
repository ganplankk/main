class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number}. : {current_question.text} (True/False)").lower().strip()
        self.question_number += 1
        self.check_collecting(answer, current_question.answer.lower().strip())

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_collecting(self, user_answer, data_answer):
        if user_answer == data_answer:
            print("You got it right ~")
            self.score += 1
            print(f"Current your Score is : {self.score}/{self.question_number}")
        else:
            print("you're answer was not collecting")

    def final_score(self):
        if len(self.question_list) == self.question_number:
            print("You've completed the quiz")
            print(f"Your final score was : {self.score}/{self.question_number}")






# TODO : asking the question
# TODO : checking if the answer was correct
# TODO : checking if we're the end of the quiz