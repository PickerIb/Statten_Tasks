#Family Name:
#Student Number:
#Course:IT1 1120
#Assignment Number 3 Part 1
#Year 2026

#Part1

######################################
#Question 1.1: Core function 
######################################


def is_up_monotone(X, d):
    """
    Print equal length pieces of X and test whether they form
    a strictly increasing numerical sequence but it makes sure X and d are
    positive integer strings and len(X) is divisible by int(d) well.
    """
    size = int(d)
    previous = None
    increasing = True
    start = 0
    first = True

    while start < len(X):
        piece = X[start:start + size]

        if not first:
            print(", ", end="")
        print(piece, end="")

        current = int(piece)

        if previous is not None and current <= previous:
            increasing = False

        previous = current
        first = False
        start += size

    print()
    return increasing


##############################################################
#Question 1.2: The User Interaction ,Main Part of the Program 
##############################################################

def is_positive_integer(s):
    """
    Return True if s represents a positive integer.
    """
    if s == "":
        return False

    if not s.isdigit():
        return False

    return int(s) > 0


def print_box(message):
    """
    Print a message surrounded by a border of stars.
    """
    width = len(message) + 4

    print("*" * width)
    print("* " + message + " *")
    print("*" * width)


def is_up_monotone(X, d):
    """
    Print equal length pieces of X and test whether they form
    a strictly increasing numerical sequence but it makes sure X and d are
    positive integer strings and len(X) is divisible by int(d) well.
    """
    size = int(d)
    previous = None
    increasing = True
    start = 0
    first = True

    while start < len(X):
        piece = X[start:start + size]

        if not first:
            print(", ", end="")

        print(piece, end="")

        current = int(piece)

        if previous is not None and current <= previous:
            increasing = False

        previous = current
        first = False
        start += size

    print()
    return increasing


def main():
    """
    Interact with the user to test up monotone number splits.
    """
    print_box("__Welcome to up-monotone inquiry__")

    name = input("What is your name? ").strip()

    print()
    print_box("__" + name + ", welcome to up-monotone inquiry.__")
    print()

    while True:
        answer = input(
            name
            + ", would you like to test if a number admits "
            + "an up-monotone split of given size? "
        ).strip().lower()

        if answer != "yes" and answer != "no":
            print("Please enter yes or no. Try again.")
            continue

        if answer == "no":
            print()
            print_box("__Good bye " + name + "!__")
            break

        print("Good choice!")

        X = input("Enter a positive integer: ").strip()

        if not is_positive_integer(X):
            print(
                "The input has to be a positive integer. "
                "Try again."
            )
            continue

        number_of_digits = len(X)

        d = input(
            "Input the split. The split has to divide the "
            "length of " + X + " i.e. "
            + str(number_of_digits) + "\n"
        ).strip()

        if not is_positive_integer(d):
            print(
                "The split has to be a positive integer. "
                "Try again."
            )
            continue

        split_size = int(d)

        if number_of_digits % split_size != 0:
            print(
                d + " does not divide "
                + str(number_of_digits) + ". Try again."
            )
            continue

        result = is_up_monotone(X, d)

        if result:
            print("The sequence is up-monotone")
        else:
            print("The sequence is not up-monotone")


main()


