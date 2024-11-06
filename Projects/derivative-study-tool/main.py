import random


class StudyGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total = 0

    def ask_question(self):
        question = random.choice(self.questions)
        print(question[0])
        answer = input("Answer: ")
        if answer == "exit":
            print("Thanks for playing!")
            print(f"Score: {self.score}/{self.total}")
            exit()
        if answer == question[1]:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"Correct answer: {question[1]}")
        self.total += 1

    def play(self):
        print("Welcome to the Derivative Study Tool!")
        print("Type 'exit' to quit.")
        while True:
            self.ask_question()


if __name__ == "__main__":
    questions = [
        ["What is the derivative of x^n?", "n*x^(n-1)"],
        ["What is the derivative of r?", "0"],
        ["What is the derivative of e^x?", "e^x"],
        ["What is the derivative of b^x?", "ln(b)*b^x"],
        ["What is the derivative of sin(x)?", "cos(x)"],
        ["What is the derivative of cos(x)?", "-sin(x)"],
        ["What is the derivative of tan(x)?", "sec(x)^2"],
        ["What is the derivative of sec(x)?", "sec(x)*tan(x)"],
        ["What is the derivative of cot(x)?", "-csc(x)^2"],
        ["What is the derivative of csc(x)?", "-csc(x)*cot(x)"],
        ["What is the derivative of ln(x)?", "1/x"],
        ["What is the derivative of log_b(x)?", "1/(x*ln(b))"],
        ["What is the derivative of arcsin(x)?", "1/sqrt(1-x^2)"],
        ["What is the derivative of arccos(x)?", "-1/sqrt(1-x^2)"],
        ["What is the derivative of arctan(x)?", "1/(1+x^2)"],
        ["What is the derivative of arcsec(x)?", "1/(|x|*sqrt(x^2-1))"],
        ["What is the derivative of arccot(x)?", "-1/(1+x^2)"],
        ["What is the derivative of arccsc(x)?", "-1/(|x|*sqrt(x^2-1))"],
        ["What is the derivative of r*f(x)?", "r*f'(x)"],
        ["What is the derivative of f(x)+-g(x)?", "f'(x)+-g'(x)"],
        ["What is the derivative of f(x)*g(x)?", "f'(x)*g(x)+f(x)*g'(x)"],
        ["What is the derivative of f(x)/g(x)?", "(f'(x)*g(x)-f(x)*g'(x))/(g(x))^2"],
        ["What is the derivative of f(g(x))?", "f'(g(x))*g'(x)"],
    ]

    game = StudyGame(questions)
    game.play()
