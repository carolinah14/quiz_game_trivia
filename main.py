from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dictionary in question_data:
    question_text = dictionary["question"]
    question_answer = dictionary["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations, you have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
