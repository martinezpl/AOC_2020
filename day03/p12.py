def takeAStep(lanes, vertical, horizontal):
    v = vertical
    h = horizontal
    while v < len(lanes):
        yield lanes[v][h]
        v += vertical
        h += horizontal
    

strings = []
with open('input.txt', 'r') as f:
    for line in f:
        if line != '\n':
            strings.append(line.strip())
        
newstrings = []
for string in strings:
    newstr = string*100
    newstrings.append(newstr)

steps = takeAStep(newstrings, 1, 3)

trees = 0
for step in steps:
    if step == '#':
        trees += 1

print(trees)
