#Family Name:Emmanuel ngabo
#Student Number:300340769
#Course:IT1 1120
#Assignment Number 4 Part 2
#Year 2026

#Part 2

########################################
#Question 2.1: Single Player Rummy Game
########################################



# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     for i in range(len(deck)):
          if i % 2 == 0:
               other.append(deck[i])
          else:
               dealer.append(deck[i])

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    processed=[]

    for card in l:
        rank=card[:-1]

        if rank not in processed:
            processed.append(rank)

            count=0

            for item in l:
                if item[:-1] == rank:
                    count=count+1

            if count % 2 == 1:
                found=False

                for item in l:
                    if item[:-1] == rank and not found:
                        no_pairs.append(item)
                        found=True

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print(" ".join(deck))

def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

     Precondition: n>=1
     '''

     number=int(input("Give me an integer between 1 and " + str(n) + ": "))

     while number < 1 or number > n:
          print("Invalid number. Please enter integer between 1 and " + str(n) + ": ")
          number=int(input("Give me an integer between 1 and " + str(n) + ": "))

     return number

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     game_over=False

     while not game_over:

          # HUMAN'S TURN
          if len(dealer) > 0 and len(human) > 0:

               print("***********************************************************")
               print("Your turn.")
               print("Your current deck of cards is:")
               print_deck(human)

               number_of_cards=len(dealer)

               print("I have " + str(number_of_cards) + " cards. If 1 stands for my first card and")
               print(str(number_of_cards) + " for my last card, which of my cards would you like?")

               choice=get_valid_input(number_of_cards)

               if choice % 100 >= 11 and choice % 100 <= 13:
                    suffix="th"
               elif choice % 10 == 1:
                    suffix="st"
               elif choice % 10 == 2:
                    suffix="nd"
               elif choice % 10 == 3:
                    suffix="rd"
               else:
                    suffix="th"

               print("You asked for my " + str(choice) + suffix + " card.")

               card=dealer.pop(choice-1)
               human.append(card)

               print("Here it is. It is " + card)
               print("With " + card + " added, your current deck is:")
               print_deck(human)

               human=remove_pairs(human)

               print("And after discarding pairs and shuffling, your deck is:")
               print_deck(human)

               wait_for_player()

               if len(human) == 0:
                    print("Ups. You do not have any more cards")
                    print("Congratulations! You, Human, win")
                    game_over=True

               elif len(dealer) == 0:
                    print("Ups. I do not have any more cards")
                    print("You lost! I, Robot, win")
                    game_over=True

          # ROBOT'S TURN
          if not game_over and len(dealer) > 0 and len(human) > 0:

               print("***********************************************************")
               print("My turn.")

               choice=random.randint(1, len(human))

               card=human.pop(choice-1)
               dealer.append(card)

               if choice % 100 >= 11 and choice % 100 <= 13:
                    suffix="th"
               elif choice % 10 == 1:
                    suffix="st"
               elif choice % 10 == 2:
                    suffix="nd"
               elif choice % 10 == 3:
                    suffix="rd"
               else:
                    suffix="th"

               print("I took your " + str(choice) + suffix + " card.")

               dealer=remove_pairs(dealer)

               wait_for_player()

               if len(dealer) == 0:
                    print("Ups. I do not have any more cards")
                    print("You lost! I, Robot, win")
                    game_over=True

               elif len(human) == 0:
                    print("Ups. You do not have any more cards")
                    print("Congratulations! You, Human, win")
                    game_over=True

          if len(dealer) == 0 and len(human) == 0:
               game_over=True


# main
play_game()
