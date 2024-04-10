import random

all_question_types = ["+", "-", "x", "/"]

score = 0
first_number = random.randrange(1, 20)
second_number = random.randrange(1, 20)
question_number = 0
question_count = 0
final_question_count = 0

def int_checker(question):
    while True:
        try:
            return int(input(question))
        except:
            print("Put a valid numbah ya muppet")


def one_question():
    global question_types, score
    question_types = random.choice(all_question_types)
    first_number = random.randrange(1, 20)
    second_number = random.randrange(1, 20)
    correct_answer = 0.0

    if question_types == "+":
        correct_answer = first_number + second_number
    elif question_types == "-":
        correct_answer = first_number - second_number
    elif question_types == "x":
        correct_answer = first_number * second_number
    elif question_types == "/":
        correct_answer = first_number / second_number
    correct_answer = round(correct_answer, 1)
    question = "What is {} {} {}? (rounded to the first decimal place)\n".format(first_number, question_types,
                                                                                 second_number)
    user_answer = float(input(question))
    user_answer = round(user_answer, 1)
    if user_answer == round(correct_answer, 1):
        print("Fah your smart!")
        score += 1
    else:
        print(f"Incorrect! yah donkey {correct_answer}")
def main():
    global question_number, question_count, final_question_count
    while True:
        game = input("Are ya ready ya pommy? (Y/N)\n").capitalize()
        if game == "Yes" or game == "Y":
            question_count = question_number + int_checker("How many questions mistah driftah?\n")
            final_question_count += question_count
            print("Lets a go")
            break

        elif game == "No" or game == "N":
            print("Too Bad monkey your playing")

        elif game == "Maybe":
            print("pick one already ya munnta!")

        else:
            print("Put a valid answer or ill rip ya a new one")


    for question_number in range(question_count):
        print(f"Question {question_number + 1}")
        one_question()

print("% ~x~x~x~x~  % Math Quiz %  ~x~x~x~x~ %")
username = input("Enter your bloody name ya punta\n").capitalize()
print("Welcome to the game {}".format(username))

main()
print("Yeah bugger off")