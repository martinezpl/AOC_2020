'''
current cup = l[0]
l.pop(1, 2, 3)
destination cup = l.index((l[0] - 1)), if popped -1

if below lowest wraps around to highest!
popped cups l[0-1, 1, 2, 3]
new current cup l[0 + 1]

labels after cup labeled 1?
'''

def part1(inp):
    cups = [int(label) for label in inp]
    moves = 1
    cc_idx = 0 #current cup index
    circ = len(cups)
    while moves < 101:
        print(' - -- - - - -- move:', moves)
        cc = cups[cc_idx]
        print(cc, cups)
        pck_idx = ((cc_idx + 1) % circ, (cc_idx + 2) % circ, (cc_idx + 3) % circ)
        print(pck_idx)
        pickup = [cups[pck_idx[0]], cups[pck_idx[1]], cups[pck_idx[2]]] 
        for c in pickup:    
            cups.remove(c)
        print('dbg:', pickup, cups)

        i = 1
        while True:
            if cc-i in cups:
                destination = cups[cups.index(cc-i)]
                break
            elif cc-i in pickup:
                i += 1
            elif cc-i < min(cups):
                destination = cups[cups.index(max(cups))]
                break
        print('destination:', destination)
        cups = cups[:cups.index(destination) + 1] + pickup + cups[cups.index(destination) + 1:]
        cc_idx = (cups.index(cc) + 1) % circ
        moves += 1
    return str(cups) 

inp = "364297581"
print(part1(inp))

