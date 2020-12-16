start = '19,20,14,0,9,1'
counted = start[:-1].split(',')
counted.pop()

countedint = [int(e) for e in counted]
def elveGame(l, last):
    cn = last # considered number
    while len(l) < 2020:
        if cn in l:
            i = len(l)
            while i > 0:
                i -= 1
                if l[i] == cn:
                    break
            a = i + 1
            l.append(cn)
            cn = len(l) - a
        else:
            l.append(cn)
            cn = 0
    return l

print(elveGame(countedint, 1))
