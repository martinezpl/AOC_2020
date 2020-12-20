class Bag:
    color = ""
    colorsInside = {}
    bagsInside = 0
 
    def __init__(self, cO, cI):
        self.color = cO
        if bool(cI):
            self.colorsInside = cI
            self.bagsInside = sum(q for q in cI.values())
            self.children = {}
            self.isEmpty = False
        else:
            self.isEmpty = True
        
    def assignChild(self, bag, quantity):
        self.children[bag] = quantity

    def showParams(self):
        return (self.color, self.colorsInside)

bags = {}

with open('input.txt', 'r') as f:
    for line in f:
        if len(line) > 1:
            line = line.strip().replace(',', "").replace('.', "").split()
            bagColor = str(line[0] + line[1])
            s = ""
            colorsInside = {}
            count = 0
            for word in line[4:]:
                if word == 'bag' or word == 'bags':
                    colorsInside[s] = count
                    s = ""
                    continue
                if word.isnumeric():
                    count = int(word)
                elif word != 'no':
                    s += word
                else:
                    break

            b = Bag(bagColor, colorsInside)
            bags[b.color] = b
flag = 0

for bag in bags.values():
    if not bag.isEmpty:
        for n, q in bag.colorsInside.items():
            bag.assignChild(bags[n], q)

ftw = []
discovered = []
def ab(bag, bagsInside, quantity):
    if bag not in discovered:
        discovered.append(bag)
        ftw.append(bagsInside * quantity)
ftw.append(len(bags['shinygold'].children))
for n, v in bags['shinygold'].children.items():
    ab(n, n.bagsInside, v)
    if not bag.isEmpty:
        for n1, v1 in bag.children.items():
            ab(n1, n1.bagsInside, v1)
            if not n1.isEmpty:
                for n2, v2 in n1.children.items():
                    ab(n2, n2.bagsInside, v2)
                    if not n2.isEmpty:
                        for n3, v3 in n2.children.items():
                            ab(n3, n3.bagsInside, v3)
                            if not n3.isEmpty:
                                for n4, v4 in n3.children.items():
                                    ab(n4, n4.bagsInside, v4)
                                    if not n4.isEmpty:
                                        for n5, v5 in n4.children.items():
                                            ab(n5, n5.bagsInside, v5)
                                            if not n5.isEmpty:
                                                for n6, v6 in n5.children.items():
                                                    ab(n6, n6.bagsInside, v6)
print(ftw)
print(sum(ftw)) 
    
    
'''
for k0, v0 in bags['shinygold'].colorsInside.items():
    flag += v0
    for k1, v1 in bags[k0].colorsInside.items():
        flag += v1
        for k2, v2 in bags[k1].colorsInside.items():
            flag += v2
            for k3, v3 in bags[k2].colorsInside.items():
                flag += v3
                for k4, v4 in bags[k3].colorsInside.items():
                    flag += v4
                    for k5, v5 in bags[k4].colorsInside.items():
                        flag += v5
'''
