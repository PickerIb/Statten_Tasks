#Family Name:Emmanuel ngabo
#Student Number:300340769
#Course:IT1 1120
#Assignment Number 4 Part 1
#Year 2026

#Part1

######################################
#Question 1: number_divisible
######################################

def number_divisible(numbers: list[int], n: int) -> int:
    """
    Type contract:
        (list[int], int) -> int

    Description:
        Counts the elements in the list that are divisible by n but make sure that 
        n must not be zero.
    """
    count = 0

    for number in numbers:
        if number % n == 0:
            count += 1

    return count

raw_input = input(
    "Please input a list of integers separated by spaces: "
).strip().split()

numbers = [int(value) for value in raw_input]

n = int(input("Please input an integer: "))

result = number_divisible(numbers, n)

print("The number of elements divisible by", n, "is", result)
