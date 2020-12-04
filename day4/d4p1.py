pN = [] # passport no. x
pN.append("")
with open('input.txt') as f:
    i = 0
    for line in f:
        if line != '\n':
            s = line.replace("\n", " ")
            pN[i] = pN[i] + s
        else:
            pN.append("")
            i += 1

pValid = 0
# I wasted 30 minutes because:
# if 'byr' and 'iyr' and ... in p:
# is apparently not equal to the syntax below:
for p in pN:
    if 'byr' in p and 'iyr' in p and 'eyr' in p and 'hgt' in p and 'hcl' in p and 'ecl' in p and 'pid' in p:    
        pValid += 1

print(pValid)

