class QuizBrain :
    def __init__(self, question_list: []) -> None :
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self) -> dict :
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Question {self.question_number+1}: {current_question.question} Is this True or False?\n").lower()
        self.question_number += 1
        if (user_answer == current_question.answer.lower()) :
            self.score += 1
            print("Correct!")
        else :
            print("Incorrect...")
            
        print(f"Current score: {self.score}/{self.question_number}\n")
        
    def still_has_questions(self) -> bool :
        return len(self.question_list) >= self.question_number + 1