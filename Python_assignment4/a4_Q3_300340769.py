#Family Name:Emmanuel ngabo
#Student Number:300340769
#Course:IT1 1120
#Assignment Number 4 Part 1
#Year 2026

#Part1

######################################
#Question 3: Longest Run
######################################


def longest_run(numbers: list[float]) -> int:
    """
    Type contract:
        (list[float]) -> int

    Description:
        Finds and returns the length of the longest
        sequence of consecutive equal values.

    """
    if len(numbers) == 0:
        return 0

    current_run = 1
    longest = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_run += 1
        else:
            current_run = 1

        if current_run > longest:
            longest = current_run

    return longest

raw_input = input(
    "Please input a list of numbers separated by spaces: "
).strip().split()

numbers = [float(value) for value in raw_input]

result = longest_run(numbers)

print(result)

