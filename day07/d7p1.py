class Bag:
    color = ""
    colorsInside = []
 
    def __init__(self, cO, cI):
        self.color = cO
        self.colorsInside = cI

    def showParams(self):
        return (self.color, self.colorsInside)

bags = []

with open('input.txt', 'r') as f:
    for line in f:
        if len(line) > 1:
            line = line.strip().replace(',', "").replace('.', "").split()
            bagColor = str(line[0] + line[1])
            s = ""
            colorsInside = []
            flag = 0
            for word in line[5:]:
                if word == 'bag' or word == 'bags':
                    colorsInside.append(s)
                    s = ""
                    continue
                if word.isnumeric():
                    pass
                else:
                    s += word   

            b = Bag(bagColor, colorsInside)
            bags.append(b)

directBags = []
for bag in bags:
    if 'shinygold' in bag.colorsInside:
        directBags.append(bag)

indirectBags = []
for bag in bags:
    for db in directBags:
        if db.color in bag.colorsInside:
            indirectBags.append(bag)

for bag in bags:
    for ib in indirectBags:
        if ib.color in bag.colorsInside:
            indirectBags.append(bag)

for bag in bags:
    for ib in indirectBags:
        if ib.color in bag.colorsInside:
            if bag not in indirectBags:
                indirectBags.append(bag)

print(len(bags))

solution = len(indirectBags) + len(directBags)
print(solution)
