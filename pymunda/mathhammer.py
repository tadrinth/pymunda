
# helper class which calculates the probabilities of certain things happening in a particular tabletop game

# it uses a lot of six sided dice
DIE = [1,2,3,4,5,6]

# if the die roll is equal to the target or higher, you hit
def hit(target):
    t = sorted([2, target, 6])[1] # clamp to 2+
    return sum(1 for x in DIE if x >= t) / len(DIE)

# roll 2d6; the target rolls D6 and adds their toughness.  if you roll equal or higher, the target is affected.
def toxin(toughness):
    hits = 0
    total = 0
    # TODO: optimize this (memoize results?)
    for i in DIE:
        for j in DIE:
            for k in DIE:
                if toughness + k <= i + j:
                    hits += 1 
                total += 1
    return hits / total

# rolls a D6, if it's a 6 or at least as high as the target's toughness, they're affected by the gas.
def gas(toughness):
    t = sorted([1, toughness, 6])[1] # clamp to 2+
    return sum(1 for x in DIE if x >= t) / len(DIE)