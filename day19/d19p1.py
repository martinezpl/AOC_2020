from more_itertools import split_at

words = []
rules = {}
with open('input.txt') as f:
    switch = False
    for l in f:
        if l == '\n':
            switch = True
            continue
        if switch == False:
            l = l.strip().split(' ')
            nr = l[0][:l[0].find(':')]
            if '"' in l[1]:
                rules[nr] = l[1][1]
            else:
                rules[nr] = l[1:]
        else:
            words.append(l.strip())

class Rule:

    def __init__(self, ID, l):
        if l == 'a' or l == 'b':
            self.val = l
        self.ID = ID
        self.branches = list(split_at(l, lambda x: x = '|'))
    
    
            
