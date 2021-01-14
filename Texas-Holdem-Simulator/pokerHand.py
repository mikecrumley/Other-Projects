# pokerHand definition

from Poker_Tuples import *
from random import shuffle
import copy
from itertools import combinations
from operator import add


class card:
    def __init__(self, kind = 'A', suit = 'S'):
        self.__kind = kind
        self.__suit = suit
    def __eq__(self, other):
        if isinstance(other,card):
            return self.__kind == other.__kind and self.__suit == other.__suit
        else:
            return False
    def set_kind(self, kind):
        self.__kind = kind
    def set_suit(self, suit):
        self.__suit = suit
    def get_kind(self):
        return self.__kind
    def get_suit(self):
        return self.__suit
    def print_card(self):
        print("{} of {}".format(self.__kind, self.__suit))


class pokerHand:
    def __init__(self, card1 = card('A','S'), card2 = card('K','S'), card3 = card('Q','S'), card4 = card('J','S'),
                 card5 = card('10','S')):
        self.__card1 = card1
        self.__card2 = card2
        self.__card3 = card3
        self.__card4 = card4
        self.__card5 = card5
    def print_cards(self):
        self.__card1.print_card()
        self.__card2.print_card()
        self.__card3.print_card()
        self.__card4.print_card()
        self.__card5.print_card()
    def get_value(self):
        kind_to_val_dict = {"2": 2, "3": 3, "4": 5, "5": 7, "6": 11, "7": 13, "8": 17, "9": 19, "10": 23, "J": 29,
                            "Q": 31, "K": 37, "A": 41}
        return kind_to_val_dict[self.__card1.get_kind()]*kind_to_val_dict[self.__card2.get_kind()]*kind_to_val_dict[self.__card3.get_kind()]* \
        kind_to_val_dict[self.__card4.get_kind()] *kind_to_val_dict[self.__card5.get_kind()]
    def is_flush(self):
        if self.__card1.get_suit() == self.__card2.get_suit() == self.__card3.get_suit() == self.__card4.get_suit() == \
                self.__card5.get_suit():
            return True
        else:
            return False
    def is_pair(self):
        kind_set = set([self.__card1.get_kind() ,self.__card2.get_kind(), \
            self.__card3.get_kind(), self.__card4.get_kind(), self.__card5.get_kind()])
        if len(kind_set) == 4:
            return True
        else:
            return False
    def is_HCST(self):
        kind_set = set([self.__card1.get_kind(), self.__card2.get_kind(), \
            self.__card3.get_kind(), self.__card4.get_kind(), self.__card5.get_kind()])
        if len(kind_set) == 5:
            if not self.is_flush():
                return True
            else:
                return False
        else:
            return False
    def get_rank(self):
        val = self.get_value()
        if self.is_pair():
            rank_index = pairvaltuple.index(val)
            rank = pairranktuple[rank_index]
        elif self.is_flush():
            rank_index = HCSTflushvaltuple.index(val)
            rank = flushranktuple[rank_index]
        elif self.is_HCST():
            rank_index = HCSTflushvaltuple.index(val)
            rank = HCSTranktuple[rank_index]
        else:
            rank_index = othvaltuple.index(val)
            rank = othranktuple[rank_index]
        return rank


init_deck_cards = [card(x[0],x[1]) for x in init_deck_list]


class deck:
    def __init__(self, cards = None):
        if cards is None:
            self.__cards = init_deck_cards
        else:
            self.__cards = cards
    def deal_card(self):
        x = self.__cards[0]
        self.__cards = self.__cards[1:len(self.__cards)]
        return x
    def show_card(self,n):
        return self.__cards[n]
    def num_cards(self):
        return len(self.__cards)
    def shuffle(self):
        shuffle(self.__cards)
    def deal_poker_hand(self):
        card1 = self.deal_card()
        card2 = self.deal_card()
        card3 = self.deal_card()
        card4 = self.deal_card()
        card5 = self.deal_card()
        return pokerHand(card1,card2,card3,card4,card5)
    def remove_card(self,card):
        x = copy.deepcopy(self.__cards)
        x.remove(card)
        self.__cards = x


def play_holdem_game(given_hands, extra_hands = 0):
    #given_hands is a list of lists of two cards, extra_hands is an integer
    new_deck = deck()
    new_deck.shuffle()
    for hand in given_hands:
        for card in hand:
            new_deck.remove_card(card)
    extra_hands_list = []
    for i in range(0,extra_hands):
        extra_hands_list = extra_hands_list + [[new_deck.deal_card(), new_deck.deal_card()]]
    board = [new_deck.deal_card(), new_deck.deal_card(), new_deck.deal_card(), new_deck.deal_card(), new_deck.deal_card()]
    def eval_hand(two_card_list):
        all_cards = two_card_list + board
        all_five_card_hands = list(combinations(all_cards,5))
        all_poker_hands = [pokerHand(*five_card_hand) for five_card_hand in all_five_card_hands]
        rank_list = [poker_hand.get_rank() for poker_hand in all_poker_hands]
        return min(rank_list)
    given_ranks = [];  extra_ranks = [];
    for given_hand in given_hands:
        given_ranks = given_ranks + [eval_hand(given_hand)]
    for extra_hand in extra_hands_list:
        extra_ranks = extra_ranks + [eval_hand(extra_hand)]
    ranks = given_ranks + extra_ranks
    winning_rank = min(ranks)
    winning_indices = [i for i, x in enumerate(ranks) if x == winning_rank]
    win_list = []
    for i in range(0,len(ranks)):
        if i in winning_indices:
            win_list = win_list + [1]
        else:
            win_list = win_list + [0]
    num_winners = len(winning_indices)
    return [x/num_winners for x in win_list]


def play_holdem(given_hands, extra_hands, num_games):
    win_list = [0]*(len(given_hands)+extra_hands)
    for i in range(0,num_games):
        new_win_list = play_holdem_game(given_hands, extra_hands)
        win_list = list( map(add, win_list, new_win_list))
    win_percentages = [x/num_games for x in win_list]
    return win_percentages





