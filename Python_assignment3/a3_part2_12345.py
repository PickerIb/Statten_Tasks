#Family Name:
#Student Number:
#Course:IT1 1120
#Assignment Number 3 Part 2
#Year 2026

#Part 2

##########################################
#Question 2.1: sum_odd_divisors(n)
##########################################

def sum_odd_divisors(n):
    """
    Return the sum of all positive odd divisors of n,
    but return None when n is zero.
    """
    if n == 0:
        return None

    total = 0
    divisor = 1
    number = abs(n)

    while divisor <= number:
        if number % divisor == 0 and divisor % 2 != 0:
            total += divisor
        divisor += 1

    return total

##########################################
#Question 2.2: series_sum()
##########################################

def series_sum():
    """
    Ask for a non negative integer n and return
    1000 plus the sum of 1/k**2 for k from 1 to n.
    Return None when n is negative.
    """
    n = int(input("Please enter a non-negative integer: "))

    if n < 0:
        return None

    total = 1000
    k = 1

    while k <= n:
        total += 1 / (k * k)
        k += 1

    return total

##########################################
#Question 2.3:pell(n)
##########################################

def pell(n):
    """
    Return the nth Pell number.
    Return None when n is negative.
    """
    if n < 0:
        return None

    if n == 0:
        return 0

    if n == 1:
        return 1

    previous = 0
    current = 1
    index = 2

    while index <= n:
        following = 2 * current + previous
        previous = current
        current = following
        index += 1

    return current

##########################################
#Question 2.4:countMembers(s)
##########################################

def countMembers(s):
    """
    Count occurrences of extraordinary characters in s,
    but  no string methods are used.
    """
    count = 0

    for ch in s:
        if ('e' <= ch <= 'j' or
                'F' <= ch <= 'X' or
                '2' <= ch <= '6' or
                ch == '!' or
                ch == ',' or
                ch == '\\'):
            count += 1

    return count

##########################################
#Question 2.5:casual_number(s)
##########################################

def casual_number(s):
    """
    Convert a whole number string with optional commas
    and an optional leading minus sign to an integer but
    return None if the string is invalid.
    """
    cleaned = ""

    for ch in s:
        if ch != ',':
            cleaned += ch

    if cleaned == "" or cleaned == "-":
        return None

    if cleaned[0] == "-":
        digits = cleaned[1:]
    else:
        digits = cleaned

    if digits == "" or not digits.isdigit():
        return None

    return int(cleaned)

##########################################
#Question 2.6:alienNumbers(s)
##########################################

def alienNumbers(s):
    """
    Return the total value of the alien numeral s.
    but  s contains only valid alien symbols.
    """
    return (s.count("T") * 1024 +
            s.count("y") * 598 +
            s.count("!") * 121 +
            s.count("a") * 42 +
            s.count("N") * 6 +
            s.count("U"))

##########################################
#Question 2.7:alienNumbersAgain(s)
##########################################

def alienNumbersAgain(s):
    """
    Calculate an alien numeral value using a loop
    without string methods.
    """
    total = 0

    for ch in s:
        if ch == "T":
            total += 1024
        elif ch == "y":
            total += 598
        elif ch == "!":
            total += 121
        elif ch == "a":
            total += 42
        elif ch == "N":
            total += 6
        elif ch == "U":
            total += 1

    return total

##########################################
#Question 2.8:encrypt(s)
##########################################

def encrypt(s):
    """
    Reverse s, then interleave characters from both ends
    of the reversed string, moving inward.
    """
    reversed_s = s[::-1]
    result = ""
    left = 0
    right = len(reversed_s) - 1

    while left <= right:
        result += reversed_s[left]

        if left < right:
            result += reversed_s[right]

        left += 1
        right -= 1

    return result

##########################################
#Question 2.9:weaveop(s)
#########################################

def weaveop(s):
    """
    Insert case sensitive o and p characters between
    consecutive alphabetic characters.
    """
    if len(s) <= 1:
        return s

    result = s[0]
    index = 0

    while index < len(s) - 1:
        first = s[index]
        second = s[index + 1]

        if first.isalpha() and second.isalpha():
            if first.isupper():
                result += "O"
            else:
                result += "o"

            if second.isupper():
                result += "P"
            else:
                result += "p"

        result += second
        index += 1

    return result
##########################################
#Question 2.10:squarefree(s)
#########################################

def squarefree(s):
    """
    Return True if s contains no substring repeated
    twice consecutively; otherwise return False.
    """
    size = 1

    while size <= len(s) // 2:
        start = 0

        while start + 2 * size <= len(s):
            first = s[start:start + size]
            second = s[start + size:start + 2 * size]

            if first == second:
                return False

            start += 1

        size += 1

    return True




