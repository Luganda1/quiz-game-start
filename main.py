from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


# for dict in question_data:
#     for key, value in dict.items():
#         v = "{}; {}".format(key, value)
#         print(v)
#         question_bank.append(v)

for dict in question_data:
    question_text = dict["question"]
    question_answer = dict["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
