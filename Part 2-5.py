#Part 2:
#1
class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

#2
class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        student_answer = raw_input(self.question + " ")
        if student_answer == self.answer:
            return True
        else:
            return False


#3
#This took me a very long time to figure out what exactly the
#question was asking me to do.
class Exam(object):
    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self, question, correct_answer):
        self.question.append(Question(question)
        self.answer.append(Question(answer))
    def administer(self):
        score = 0
        for question in self.questions:
            score_tally = question.ask_and_evaluate()
            if score_tally == True:
                score = score + 1
        return score

        
# Part 4


def take_test(exam, student):
    student.score = exam.administer()

def example():
    #believe this would be the way to create new instance 
    new_test = Exam()
    new_test.add_question("Who was our Nation's first President?", "George Washinton")
    Cristina_Clarkin = Student("Cristina", "Clarkin", "899 Pine St.")
    take_test(new_test, 'Cristina')


# Part 5
class Quiz(Exam):
    def administer(self):
        #calls administer method on quiz
        score = super(Quiz, self).administer()
        for question in self.questions:
            score_tally = (float(len(self.questions) / 2)
            if score > score_tally:
                return True
            else:
                return false

        


