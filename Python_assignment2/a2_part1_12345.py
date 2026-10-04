#Family Name:
#Student Number:
#Course:IT1 1120
#Assignment Number 2 Part 1
#Year 2026

#Part1

######################################
#Question 1.1: Elementary school quiz
######################################

import random
import math

def elementary_school_quiz(flag, n):
    """
    Generate math practice questions involving powers of 2
    or logarithms with base 2 flag when is equal to 0 means
    logarithm questions while when flag is equal to 1 means
    exponentiation questions and then return the number of
    correct answers.
    """
    correct_answers = 0

    for i in range(n):
        number = random.randint(0, 10)

        if flag == 0:
            result = 2 ** number

            answer = input(
                f"Question {i + 1}:\n"
                f"2 to what is {result} "
                f"i.e. what is the result of log_2 ({result})? "
            )

            if answer.strip() == str(number):
                correct_answers += 1

        elif flag == 1:
            result = 2 ** number

            answer = input(
                f"Question {i + 1}:\n"
                f"What is the result of 2^{number}? "
            )

            if answer.strip() == str(result):
                correct_answers += 1

    return correct_answers


##########################################
#Question 1.2:High School Equation Solver
#########################################

def high_school_quiz(a, b, c):
    """
    This function display the equation together with its solutions
    including quadratic, linear, identity, and no-solution cases.
    """
    if a == 0:
        if b == 0:
            print(f"The quadratic equation {a}·x + {c} = 0")
            if c == 0:
                print("is satisfied for all numbers x")
            else:
                print("is satisfied for no number x")
        else:
            root = -c / b
            print(f"The linear equation {b}·x + {c} = 0")
            print(f"has the following root/solution: {root}")
        return

    print(f"The quadratic equation {a}·x^2 + {b}·x + {c} = 0")
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("has the following real roots:")
        print(x1, "and", x2)

    elif discriminant == 0:
        x = -b / (2 * a)
        print("has only one solution, a real root:")
        print(x)

    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / abs(2 * a)
        print("has the following two complex roots:")
        print(f"{real_part} + i {imaginary_part}")
        print("and")
        print(f"{real_part} - i {imaginary_part}")

print("*" * 43)
print("*  Welcome to my math quiz-generator  *")
print("*" * 43)

name = input("What is your name? ")

print(f"Hi {name}. Are you in? Enter")
print("1 for elementary school")
print("2 for high school or")
print("3 or other character(s) for none of the above?")

choice = input()

if choice == "1":
    print("*" * 76)
    print(f"* {name}, welcome to my quiz-generator for elementary school students. *")
    print("*" * 76)

    print(f"{name} what would you like to practice? Enter")
    print("0 for inverse of exponentiation")
    print("1 for exponentiation")

    flag = input()

    if flag not in ["0", "1"]:
        print("Invalid choice. Only 0 or 1 is accepted.")
        print(f"Good bye {name}!")

    else:
        n = input(
            "How many practice questions would you like to do? "
            "Enter 0, 1, or 2: "
        )

        if n not in ["0", "1", "2"]:
            print("Only 0, 1, or 2 are valid choices.")
            print(f"Good bye {name}!")

        elif n == "0":
            print("Zero questions. OK. Good bye")
            print(f"Good bye {name}!")

        else:
            flag = int(flag)
            n = int(n)

            print(f"{name}, here is your {n} questions:")
            score = elementary_school_quiz(flag, n)

            if score == n:
                print(f"Congratulations {name}! You'll probably get an A tomorrow.")
            elif score == n / 2:
                print(f"You did ok {name}, but I know you can do better.")
            else:
                print(f"I think you need some more practice {name}.")

            print(f"Good bye {name}!")

elif choice == "2":
    print("*" * 72)
    print(f"* quadratic equation, a·x^2 + b·x + c= 0, solver for {name} *")
    print("*" * 72)

    while True:
        response = input(
            f"{name}, would you like a quadratic equation solved? "
        )

        if response.strip().lower() != "yes":
            break

        print("Good choice!")

        a = float(input("Enter a number the coefficient a: "))
        b = float(input("Enter a number the coefficient b: "))
        c = float(input("Enter a number the coefficient c: "))

        high_school_quiz(a, b, c)

    print(f"Good bye {name}!")

else:
    print(f"{name} you are not a target audience for this software.")
    print(f"Good bye {name}!")
