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
for p in pN:
    pF = {} # passport fields
    fields = p.split()
    i = 0
    while i < len(fields):
        field = fields[i]
        entry = field[:field.find(':')]
        value = field[field.find(':') + 1:]
        try:
            if value[0] == '0':
                pf[entry] = value
            else:
                pF[entry] = int(value)
        except:
            pF[entry] = value
        i += 1

    vP = 0 # Validating points
    if 'byr' in pF:
        s = pF['byr']
        if s >= 1920 and s <= 2002:
            vP += 1

    if 'iyr' in pF:
        s = pF['iyr']
        if s >= 2010 and s <= 2020:
            vP +=1

    if 'eyr' in pF:
        s = pF['eyr']
        if s >= 2020 and s <= 2030:
            vP +=1

    if 'hgt' in pF:
        s = pF['hgt']
        if type(s) is not int:
            num = ""
            for ch in s:
                if ch.isdigit():
                    num = num + ch
                else:
                    num = int(num)
                    if ch == 'c':
                        if num >= 150 and num <= 193:
                            vP += 1
                    elif ch == 'i':
                        if num >= 59 and num <= 76:
                            vP += 1
    if 'hcl' in pF:
        s = str(pF['hcl'])
        if len(s) == 7 and s[0] == '#':
            points = 0
            for ch in s[1:]:
                if (ord(ch) >= ord('a') and ord(ch) <= ord('f')) or (ord(ch) >= ord('0') and ord(ch) <= ord('9')):
                    points += 1
            if points == 6:
                vP += 1

    if 'ecl' in pF:
        s = pF['ecl']
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for color in colors:
            if s == color:
                vP += 1
                break

    if 'pid' in pF:
        s = str(pF['pid'])
        if s.isdigit() and len(s) == 9:
            vP += 1

    if vP == 7:
        pValid += 1

print(pValid)
