
def choose(rack, kept, prevscore):

    pull = []

    # Always pull all 4s
    while 4 in rack:
        rack.remove(4)
        pull.append(4)

    # If we got something and there are plenty
    # of dice left we're done.
    if len(pull) > 0 and len(rack) > 2:
        return pull

    # Take ones
    while 1 in rack:
        rack.remove(1)
        pull.append(1)

    # Quit if we have something.
    if len(pull) > 0:
        return pull

    # Sort the rack.
    rack.sort()

    # Return the lowest die.
    return [rack[0]]
