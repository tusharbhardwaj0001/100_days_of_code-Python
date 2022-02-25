from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

new_Question = []
for q in question_data:
    question_text = q["text"]
    answer_answer = q["answer"]
    n_Question = Question(question_text, answer_answer)
    new_Question.append(n_Question)

quiz = QuizBrain(new_Question)
while quiz.is_still_Question():
    quiz.nextQuestion()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
