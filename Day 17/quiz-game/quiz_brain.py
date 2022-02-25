class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def is_still_Question(self):
        return self.question_number < len(self.question_list)
    
    def nextQuestion(self):
        currentQuestion = self.question_list[self.question_number]
        userAnswer = input(f"Q.{self.question_number + 1}: {currentQuestion.question} (True/False)?: ")
        self.checkAnswer(userAnswer, currentQuestion.answer)
        self.question_number += 1

    def checkAnswer(self,userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("You got it right!")
            print(f"The correct answer was: {correctAnswer}")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number + 1}")
        else:
            print("That's wrong!")
            print(f"The correct answer was: {correctAnswer}")
            print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")
