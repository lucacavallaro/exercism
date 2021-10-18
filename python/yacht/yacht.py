"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12

kind_score_fn = lambda n : lambda dice : n * dice.count(n)
straight_score_fn = lambda c : lambda dice: 30 if sorted(dice) == c else 0

def four_of_a_kind_score(dice):
    for (kind, occ) in Counter(dice).items():
        if occ >= 4:
            return kind * 4
    return 0

compute_score = {
    YACHT: lambda dice: 50 if sum(dice) == dice[0] * 5 else 0,
    ONES: kind_score_fn(1),
    TWOS: kind_score_fn(2),
    THREES: kind_score_fn(3),
    FOURS: kind_score_fn(4),
    FIVES: kind_score_fn(5),
    SIXES: kind_score_fn(6),
    FULL_HOUSE: lambda dice : sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0,
    FOUR_OF_A_KIND: four_of_a_kind_score,
    LITTLE_STRAIGHT: straight_score_fn([1, 2, 3, 4, 5]),
    BIG_STRAIGHT: straight_score_fn([2, 3, 4, 5, 6]),
    CHOICE: lambda dice: sum(dice),
}

def score(dice, category):
    return compute_score[category](dice)
    
