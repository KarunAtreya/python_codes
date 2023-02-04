class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def check_answer(self, answer, current_answer):
        if answer == current_answer:
            print("You are right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"Correct answer is {answer}")
        print(f"Score is:({self.score}/{self.question_number})")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.N.{self.question_number}:{current_question.text} (True/False):"
        )
        self.check_answer(current_question.answer, answer)

    def still_has_questions(self, question_list):
        return self.question_number < len(self.question_list)
