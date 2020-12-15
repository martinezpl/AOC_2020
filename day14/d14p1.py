masks = {}

with open('input.txt') as f:
    mems = []
    current_mask = ""
    for line in f:
        if line != '\n':
            s = line.strip()
            if s[1] == 'a':
                masks[current_mask] = mems
                mems = []
                current_mask = s[7:]
            else:
                mems.append(s[4:])

    masks[current_mask] = mems

memory_cells = {}
print(masks.keys())
for mask, mems in masks.items():
    for m in mems:
        cmask = mask
        addr = m[:m.find(']')]
        bv = list(f"{int(m[m.find('=') + 2:]):b}")
        bv = [0] * (len(cmask) - len(bv)) + bv
        cmask = list(cmask)
        i = len(cmask) - 1
        while i >= 0:
            if cmask[i] == 'X':
                cmask[i] = bv[i]
            i -= 1
        memory_cells[addr] = ''.join(map(str, cmask))

summie = 0
for v in memory_cells.values():
    summie += int(v, 2)

print(summie)
