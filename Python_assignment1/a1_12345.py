#Family Name:
#Student Number:
#Course:IT1 1120
#Assignment Number 1
#Year 2026



##################
# Question 1
##################

def mh2kh(s):
    """
    This function  is used to convert miles per hour to kilometres per hour
    but s is number to be used and make sure it's positive number.
    """
    return s * 1.60934

##################
# Question 2
##################

import math
def pythagorean_pair(a,b):
    """
    Return True if a and b form a Pythagorean pair, and False otherwise.
    but a and b must be integers.
    """
    c=math.sqrt(a**2 + b**2)
    return c== int(c)

##################
# Question 3
##################

def in_out(xs, ys, side):
    """
    Ask for the x and y coordinates of a point and print True if
    the point is inside or on the boundary of the square but make sure side is non negative.
    
    """
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))

    inside = (xs <= x) and (x <= xs + side) and \
             (ys <= y) and (y <= ys + side)

    print(inside)
    
##################
# Question 4
##################

def safe(n):
    """
    Return True if n is a safe number and False otherwise.
    A number is unsafe if it contains digit 9 or is divisible by 9.
    make sure number is a non-negative integer with at most two digits.
    """
    tens = n // 10
    units = n % 10

    return (tens != 9) and (units != 9) and (n % 9 != 0)

##################
# Question 5
##################

def quote_maker(quote, name, year):
    """
    Return a sentence containing the quote, name, and year.
    but quote and name are strings and year is a number.
    """
    return 'In ' + str(year) + ', a person called ' + name + \
           ' said: "' + quote + '"'

##################
# Question 6
##################

def quote_displayer():
    """
    Ask the user for a quote, name, and year, then display
    the formatted quotation using quote_maker().
    """
    quote = input("Give me a quote: ")
    name = input("Who said that? ")
    year = int(input("What year did she/he say that? "))

    print(quote_maker(quote, name, year))

##################
# Question 7
##################

def rps_winner():
    """
    Ask both players for their rock, paper, or scissors choices
    and display whether player 1 wins and whether the game is a tie.
    """
    player1 = input(
        "What choice did player 1 make?\n"
        "Type one of the following options: rock, paper, scissors: "
    )

    player2 = input(
        "What choice did player 2 make?\n"
        "Type one of the following options: rock, paper, scissors: "
    )

    player1_wins = (
        (player1 == "rock" and player2 == "scissors") or
        (player1 == "paper" and player2 == "rock") or
        (player1 == "scissors" and player2 == "paper")
    )

    tie = player1 == player2

    print("Player 1 wins. That is", player1_wins)
    print("It is a tie. That is", tie)

##################
# Question 8
##################

def fun(x):
    """
    Solve 10**(4*y) = x + 3 for y and return y.
    make sure x is positive.
    """
    return math.log10(x + 3) / 4


##################
# Question 9
##################


def ascii_name_plaque(name):
    """
    Print an ASCII name plaque containing name.
    make sure that  name is a string.
    """
    width = len(name) + 10
    border = "*" * width
    empty = "*" + " " * (width - 2) + "*"
    middle = "* __" + name + "__ *"

    print(border)
    print(empty)
    print(middle)
    print(empty)
    print(border)

##################
# Question 10
##################

import turtle


def draw_house():
    """
    Draws a house using the Turtle graphics module.
    The house contains a roof, door, square window,
    circular window  and chimney with coloured regions.
    There are no parameters.
    """

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(3)
    
    # House body

    t.penup()
    t.goto(-180, -120)
    t.pendown()

    t.goto(180, -120)
    t.goto(180, 70)
    t.goto(-180, 70)
    t.goto(-180, -120)

    # Roof

    t.penup()
    t.goto(-200, 70)
    t.pendown()

    t.goto(-100, 180)
    t.goto(100, 175)
    t.goto(210, 70)
    t.goto(180, 70)
    t.goto(100, 175)
    t.goto(20, 70)
    t.goto(-180, 70)

    # Chimney 

    t.penup()
    t.goto(130, 125)
    t.pendown()

    t.goto(130, 205)
    t.goto(165, 205)
    t.goto(165, 105)
    t.goto(130, 125)

    # Door


    t.penup()
    t.goto(-110, -120)
    t.pendown()

    t.goto(-110, 15)
    t.goto(-40, 15)
    t.goto(-40, -120)

    # Door knob
    t.penup()
    t.goto(-52, -55)
    t.pendown()
    t.dot(5)

    # Square window

    t.penup()
    t.goto(95, -10)
    t.pendown()

    t.fillcolor("blue")
    t.begin_fill()

    t.goto(155, -10)
    t.goto(155, 50)
    t.goto(95, 50)
    t.goto(95, -10)

    t.end_fill()

    # Window cross
    t.penup()
    t.goto(125, -10)
    t.pendown()
    t.goto(125, 50)

    t.penup()
    t.goto(95, 20)
    t.pendown()
    t.goto(155, 20)

    # Circular window

    t.penup()
    t.goto(105, 110)
    t.pendown()

    t.fillcolor("blue")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    # Ground line

    t.penup()
    t.goto(-220, -120)
    t.pendown()

    t.goto(220, -120)

    t.penup()

    turtle.done()

##################
# Question 11
##################

def alogical(n):
    """
    Return the minimum number of times n must be divided by 2
    to obtain a value less than or equal to 1.
    make sure that  n is greater than or equal to 1.
    """
    return math.ceil(math.log(n, 2))

##################
# Question 12
##################

def cad_cashier(price, payment):
    """
    Return the change owed after rounding to the nearest
    five cents in Canadian currency.
    make sure that  payment is greater than or equal to price.
    """
    change = payment - price
    return round(change * 20) / 20

##################
# Question 13
##################

def min_CAD_coins(price, payment):
    """
    Return the minimum number of Canadian toonies, loonies,
    quarters, dimes, and nickels needed to make the change.
    make sure the payment is greater than or equal to price.
    """
    change = cad_cashier(price, payment)
    cents = int(round(change * 100))

    toonies = cents // 200
    cents = cents % 200

    loonies = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5

    return (toonies, loonies, quarters, dimes, nickels)

