'''
--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

'''

fields = {}
nt = {}
t = []
with open('input.txt') as f:
    j = 1
    for line in f:
        if line != '\n':
            fn = "" # field name
            rn = "" # ranges
            i = 0
            if not line[0].isnumeric():
                s = line.split()
                while i < len(s):
                    if ':' in fn:
                        rn += s[i]
                        i += 1
                    while ':' not in fn:
                        fn += s[i]
                        i += 1
                    fields[fn] = rn
            else:
                s = line.strip().split(',')
                sint = []
                for n in s:
                    sint.append(int(n))
                if not 'nearbytickets:' in fields:
                    t = sint
                else:
                    nt[j] = sint
                    j += 1


del fields['nearbytickets:']
del fields['yourticket:']

#organize field ranges
r = []
for f, s in fields.items():
    fr = s[:s.find('o')].split('-')
    sr = s[s.find('r')+1:].split('-')
     
    lr = list(range(int(fr[0]), int(fr[1]))) + list(range(int(sr[0]), int(sr[1])))
    fields[f] = lr
    r += lr

#find and delete invalid tickets
r = set(r)
blacklist = []
for k, v in nt.items():
    for num in v:
        if num not in r:
            blacklist.append(k)
            break

for x in blacklist:
    del nt[x] 

#organize fields in nearby tickets
columns = {}
while i < len(t):
    columns[i] = []
    i += 1

for ticket in nt.values():
    i = 0
    while i < len(t):
        columns[i].append(ticket[i])
        i += 1

#compare ranges
ordered_ticket = {}
i = 0

def belongsTo(arr1, arr2):
    i = 0
    for n in arr1:
        if n in arr2:
            i += 1
    if i == len(arr1):
        return True
    else:
        return False

solution = 1
i = -1
f2 = fields.copy()
for c in columns.values():
    i += 1
    for f, r in f2.items():
        if belongsTo(c, r):
            ordered_ticket[f] = t[i]
            del f2[f]
            if f[:9] == 'departure':
                solution *= t[i]
            break

print(ordered_ticket)
print(len(t), len(ordered_ticket), len(columns.keys()))
print(solution)
