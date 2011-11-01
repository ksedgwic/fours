#!/bin/env python

import sys
import copy
import random

def error(str):
    """Report an error and exit"""
    print str
    sys.exit(1)

def roll(ndice):
    """Roll N dice"""
    dice = []
    for ii in range(0, ndice):
        dice.append(random.randrange(1, 7))
    return dice

def turn(nm, lcls, pscore):
    """Run a players full turn"""

    # Start with an empty kept array.
    kept = []

    # Start with score of 0.
    score = 0

    # Start with 5 dice.
    ndice = 5

    # Player keeps going till all dice are kept.
    while ndice > 0:

        # Roll the dice
        rack = roll(ndice)

        # Pass copies of the arrays to prevent cheating.
        rtmp = copy.deepcopy(rack)
        ktmp = copy.deepcopy(kept)

        # Print the rack
        print nm + ": " + str(rack) + ' ' + str(kept) + ' ->',

        # Call the player to choose keepers.
        pulled = lcls['choose'](rtmp, ktmp, pscore)

        # RULE - you must choose something.
        if len(pulled) == 0:
            error("empty choice")

        # Print the returned value.
        print str(pulled) + ' : ',

        # Remove the chosen elements from the rack and add to kept.
        while len(pulled):
            vv = pulled.pop()
            try:
                rack.remove(vv)
            except ValueError, ex:
                # RULE - you can only keep what you got.
                error("non-existent value " + str(vv))

            # Inserting at the beginning of the kept looks nicer.
            kept.insert(0, vv)

            # Update the score.
            if vv != 4:
                score += vv

            # One less die in the rack.
            ndice -= 1

        # Print the returned value.
        print str(score)

        # Print the kept and the score at the end of the line.
        # print '-> ' + str(kept) + ': ' + str(score)
    
    # When we're all done, return the score.
    return score
