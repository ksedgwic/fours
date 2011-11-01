Fours
----------------------------------------------------------------

The fours program runs a simple game cycle:

    [ksedgwic@lap3 fours]$ ./fours simple.py simple.py 
    simple.py: [1, 4, 6, 1, 3] -> [4] -> [4]: 0
    simple.py: [6, 2, 2, 6] -> [2] -> [2, 4]: 2
    simple.py: [6, 5, 4] -> [4] -> [4, 2, 4]: 2
    simple.py: [6, 6] -> [6] -> [6, 4, 2, 4]: 8
    simple.py: [4] -> [4] -> [4, 6, 4, 2, 4]: 8

    simple.py: [1, 5, 1, 2, 4] -> [4] -> [4]: 0
    simple.py: [6, 6, 1, 1] -> [1, 1] -> [1, 1, 4]: 2
    simple.py: [4, 4] -> [4, 4] -> [4, 4, 1, 1, 4]: 2


Stats
----------------------------------------------------------------

Currently the program runs 10K turns and tabulates the average
and median scores.

Example run:

    ./stats simple.py

    ... [lots bobitted] ...

    simple.py: [2, 6, 3, 3, 4] -> [4] -> [4]: 0
    simple.py: [3, 2, 5, 1] -> [1] -> [1, 4]: 1
    simple.py: [5, 1, 1] -> [1, 1] -> [1, 1, 1, 4]: 3
    simple.py: [2] -> [2] -> [2, 1, 1, 1, 4]: 5

    simple.py: [3, 3, 1, 2, 5] -> [1] -> [1]: 1
    simple.py: [4, 2, 4, 2] -> [4, 4] -> [4, 4, 1]: 1
    simple.py: [1, 6] -> [1] -> [1, 4, 4, 1]: 2
    simple.py: [3] -> [3] -> [3, 1, 4, 4, 1]: 5

    average score is 6.129
    median score is 6.000


Take a look at the simple.py strategy and see if you can
do better!
