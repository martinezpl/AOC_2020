with open('input.txt') as f:
    rl = f.readlines()
    p1 = [int(l.strip()) for l in rl[1:rl.index('\n')]] 
    p2 = [int(l.strip()) for l in rl[rl.index('\n') + 2:] if l != '\n']


while len(p1) != 0 and len(p2) != 0:
    print(p1, p2)
    if p1[0] > p2[0]:
        p1.append(p1.pop(0))
        p1.append(p2.pop(0))
    elif p1[0] < p2[0]:
        p2.append(p2.pop(0))
        p2.append(p1.pop(0))


winner = max((p1, p2))
i = len(winner)
score = 0
print(winner)
for card in winner:
    score += int(card) * i
    i -= 1

print(score)
