from Poker_Tuples import *
from pokerHand import *

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print("\n")
print("This is a Texas Hold'em simulator.  The user may specify any number of two-card starting hands, \
any number of randomly drawn hands (up to ten total, with random hands chosen at the start of each game), \
and any number of games to be played. \
The hands play against each other \"all in\"; that is, it simply deals a 5 card board and \
evaluates the winning hand.  Thus, these winning percentages are good approximations of \'pre-flop odds'.\n")
print("Please select kinds from among 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A and suits from among S, C, H, D.\n")
print("A note on performance: A 10 hand, 10,000 game simulation takes about 2 minutes.\n")

play = "Y"

while play == "y" or play == "Y":
    print("How many hands would you like to specify?")
    success = 0
    while success == 0:
            num_spec_hands = input()
            if num_spec_hands in ('1','2','3','4','5','6','7','8','9','10'):
                success = 1
                num_spec_hands = int(num_spec_hands)
            else:
                print("Error, please type an integer between 1 and 10.")
    max_rand_hands = 10 - num_spec_hands
    success = 0
    while success == 0:
        if max_rand_hands == 0:
            break
        print("\nHow many random hands would you like to play?")
        num_random_hands = input()
        if num_random_hands in list(map(str,list(range(0,max_rand_hands+1)))):
            success = 1
            num_random_hands = int(num_random_hands)
        else:
            print("Error, please type and integer between ", 0, " and ", max_rand_hands)
    given_hands = []
    card_list = []
    for i in range(1,num_spec_hands+1):
        card1indic = 0
        while card1indic == 0:
            success = 0
            while success == 0:
                print("\nHand",i,",card 1 kind:")
                card1kind = input()
                if card1kind in kind_tuple:
                    success = 1
                else:
                    print("Error, please input a valid kind.")
            success = 0
            while success == 0:
                print("\nHand",i,",card 1 suit:")
                card1suit = input()
                if card1suit in suit_tuple:
                    success = 1
                else:
                    print("Error, please input a valid suit.")
            card1 = card(card1kind,card1suit)
            if card1 in card_list:
                print("Error, card already taken.")
            else:
                card1indic = 1
                card_list = card_list + [card1]
        card2indic = 0
        while card2indic == 0:
            success = 0
            while success == 0:
                print("\nHand",i,",card 2 kind:")
                card2kind = input()
                if card2kind in kind_tuple:
                    success = 1
                else:
                    print("Error, please input a valid kind.")
            success = 0
            while success == 0:
                print("\nHand",i,",card 2 suit:")
                card2suit = input()
                if card2suit in suit_tuple:
                    success = 1
                else:
                    print("Error, please input a valid suit.")
            card2 = card(card2kind,card2suit)
            if card2 in card_list:
                print("Error, card already taken.")
            else:
                card2indic = 1
                card_list = card_list + [card2]
        given_hands = given_hands + [[card1, card2]]
    print("\nStarting hands successfully specified.  How many games would you like to simulate?")
    indic = 0
    while indic == 0:
        num_games = input()
        if not RepresentsInt(num_games):
            print("Error, please input a positive integer.")
            continue
        else:
            pass
        num_games = int(num_games)
        if num_games < 1:
            print("Error, please input a positive integer.")
            continue
        else:
            pass
        indic = 1
    print("\nSimulating...")
    winning_percentages = play_holdem(given_hands, num_random_hands, num_games)
    print("\nWinning Percentages:\n")
    for i in range(0,len(given_hands)):
        card1 = given_hands[i][0]
        card2 = given_hands[i][1]
        print(card1.get_kind(), "of", card1.get_suit(), ",", card2.get_kind(), \
              "of", card2.get_suit(),": ", winning_percentages[i])
    for i in range(0,num_random_hands):
        print("Random hand", i+1, ":", winning_percentages[i+num_spec_hands])
    print("\nWould you like to play again? (Y/N)")
    play = input()
    print("\n")
print("Thank you for playing!")
input()


