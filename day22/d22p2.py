with open('input.txt') as f:
    rl = f.readlines()
    p1 = [int(l.strip()) for l in rl[1:rl.index('\n')]] 
    p2 = [int(l.strip()) for l in rl[rl.index('\n') + 2:] if l != '\n']

def combat(p1, p2):
    mem1 = []
    mem2 = []
    while len(p1) != 0 and len(p2) != 0:
        if tuple(p1) in mem1 or tuple(p2) in mem2:
            return 0, p1
        else:
            mem1.append(tuple(p1))
            mem2.append(tuple(p2))
        
        win = int(p1[0] < p2[0])
        if len(p1) - 1 >= p1[0] and len(p2) - 1 >= p2[0]:
            print(p1, p2)
            win, d = combat(p1[1:p1[0] + 1], p2[1:p2[0] + 1])
        if win == 0:
            p1.append(p1.pop(0))
            p1.append(p2.pop(0))
        elif win == 1:
            p2.append(p2.pop(0))
            p2.append(p1.pop(0))
    if p1 > p2:
        return 0, p1
    elif p1 < p2:
        return 1, p2

score = 0
x, winner = combat(p1, p2)
i = len(winner)
for card in winner:
    score += int(card) * i
    i -= 1

print(score)
