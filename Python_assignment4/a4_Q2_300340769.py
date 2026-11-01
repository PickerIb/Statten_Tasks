#Family Name:Emmanuel ngabo
#Student Number:300340769
#Course:IT1 1120
#Assignment Number 4 Part 1
#Year 2026

#Part1

######################################
#Question 2: Two-Length Run 
######################################


def two_length_run(numbers: list[float]) -> bool:
    """
    Type contract:
        (list[float]) -> bool

    Description:
        Checks whether the list contains at least
        one run of two or more consecutive equal values.

    """
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            return True

    return False

raw_input = input(
    "Please input a list of numbers separated by spaces: "
).strip().split()

numbers = [float(value) for value in raw_input]

result = two_length_run(numbers)

print(result)
