#!/bin/env python

import sys

def choose(rack, kept, prevscore):

    global sys

    print '',
    
    line = sys.stdin.readline().rstrip()
    pullstritems = line.split(',')
    pull = []
    for pullstr in pullstritems:
        pull.append(int(pullstr))

    return pull
