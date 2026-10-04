#Family Name:
#Student Number:
#Course:IT1 1120
#Assignment Number 2 Part 2
#Year 2026

#Part 2

##########################################
#Question 2.1: Minimum Enclosing Rectangle
##########################################

def min_enclosing_rectangle(radius, x, y):
    """
    Calculate the bottom left corner of the smallest
    axis aligned rectangle containing the circle and
    make sure that radius is positive number because
    when it i negative returns none.
    """
    if radius < 0:
        return None
    bottom_left_x = x - radius
    bottom_left_y = y - radius
    return (bottom_left_x, bottom_left_y)

##########################################
#Question 2.2: Vote Percentage
##########################################


def vote_percentage(results):
    """
    Count yes and no substrings in the results string.
    Return the proportion of yes votes and make sure
    that results contains at least one yes or no vote.
    """
    yes_count = results.count("yes")
    no_count = results.count("no")
    total_votes = yes_count + no_count
    return yes_count / total_votes

##########################################
#Question 2.3:  Voting Outcome
##########################################
def vote():
    """
    This function ask the user for yes, no, and abstained votes.
    then it calculate the percentage of yes votes using
    vote_percentage() and print the voting outcome.
    """
    results = input(
        "Enter the yes, no, abstained votes one by one "
        "and then press enter:\n"
    )
    percentage = vote_percentage(results)
    yes_count = results.count("yes")
    no_count = results.count("no")
    if yes_count == yes_count + no_count:
        print("proposal passes unanimously")
    elif percentage >= 2 / 3:
        print("proposal passes with super majority")
    elif percentage >= 1 / 2:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")

##########################################
#Question 2.4:  Convert Number into (l, o)
##########################################
        
def l2lo(w):
    """
    Convert the non negative number w into (l, o) so that w = l + o/16, where l is an integer and o is from 0 to 15.
    """
    l = int(w)
    o = (w - l) * 16
    return (l, o)

