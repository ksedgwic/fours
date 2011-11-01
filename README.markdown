Fours
----------------------------------------------------------------

The fours program runs a simple game cycle between two scripts:

    ./fours simple.py simple.py 
    simple.py: [1, 3, 3, 5, 2] [] -> [1] :  1
    simple.py: [6, 2, 3, 5] [1] -> [2] :  3
    simple.py: [5, 3, 6] [2, 1] -> [3] :  6
    simple.py: [4, 3] [3, 2, 1] -> [4] :  6
    simple.py: [4] [4, 3, 2, 1] -> [4] :  6

    simple.py: [4, 4, 6, 5, 4] [] -> [4, 4, 4] :  0
    simple.py: [5, 4] [4, 4, 4] -> [4] :  0
    simple.py: [4] [4, 4, 4, 4] -> [4] :  0



Stats
----------------------------------------------------------------

Currently the program runs 10K turns on one script and tabulates the
average and median scores.

Example run:

    ./stats simple.py

    ... [lots bobitted] ...

    simple.py: [2, 5, 5, 4, 5] [] -> [4] :  0
    simple.py: [5, 6, 1, 4] [4] -> [4] :  0
    simple.py: [2, 5, 3] [4, 4] -> [2] :  2
    simple.py: [2, 6] [2, 4, 4] -> [2] :  4
    simple.py: [4] [2, 2, 4, 4] -> [4] :  4

    simple.py: [4, 3, 4, 6, 2] [] -> [4, 4] :  0
    simple.py: [3, 5, 2] [4, 4] -> [2] :  2
    simple.py: [1, 2] [2, 4, 4] -> [1] :  3
    simple.py: [3] [1, 2, 4, 4] -> [3] :  6

    average score is 6.168
    median score is 6.000


Human Player
----------------------------------------------------------------

You can play manually in place of on of the prrograms:

    ./fours simple.py human.py
    simple.py: [5, 4, 1, 5, 4] [] -> [4, 4] :  0
    simple.py: [6, 3, 5] [4, 4] -> [3] :  3
    simple.py: [1, 5] [3, 4, 4] -> [1] :  4
    simple.py: [1] [1, 3, 4, 4] -> [1] :  5

    human.py: [3, 1, 3, 1, 5] [] -> 1
     [1] :  1
    human.py: [4, 5, 3, 4] [1] -> 4, 4
     [4, 4] :  1
    human.py: [2, 6] [4, 4, 1] -> 2
     [2] :  3
    human.py: [6] [2, 4, 4, 1] -> 6
     [6] :  9

Apologies for the formatting of the human turns ...
