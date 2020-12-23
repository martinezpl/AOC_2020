t_b = {} # tile_borders
mtx = []
with open('input.txt') as f:
    tile = []
    for l in f:
        if l == '\n':
            mtx.append(tile.copy())
            tile.clear()
        else:
            tile.append(l.strip())

# extract borders 
for t in mtx:
    ls = ""
    rs = "" # left/right side
    for s in t[1:]:
        ls += s[0]
        rs += s[-1]
    t_b[t[0][5:9]] = (t[1], ls, t[-1], rs)

solution = 1
for til, brd in t_b.items():
    comp = t_b.copy()
    comp.pop(til)
    count = 0
    for brdc in comp.values():
        if brd[0] in brdc or brd[0][::-1] in brdc:
            count += 1
        elif brd[1] in brdc or brd[1][::-1] in brdc:
            count += 1
        elif brd[2] in brdc or brd[2][::-1] in brdc:
            count += 1
        elif brd[3] in brdc or brd[3][::-1] in brdc:
            count += 1
    if count == 2:
        solution *= int(til)

print(solution)
