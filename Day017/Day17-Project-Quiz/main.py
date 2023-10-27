from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def import_data() -> [] :
    question_bank = []
    for question in question_data :
        new_entry = Question(question["text"], question["answer"])
        question_bank.append(new_entry)
    print(f"{len(question_bank)} questions loaded...")
    return question_bank

question_bank = import_data()
quiz_controller = QuizBrain(question_bank)

while quiz_controller.still_has_questions() == True : quiz_controller.next_question()