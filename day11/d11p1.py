import numpy as np

with open('input.txt') as f:
    seat_map = np.array([])
    a = 0
    for line in f:
        a += 1
        l = []
        for ch in line.strip():
            l.append(ch)
        if len(l) > 0:
            try:
                seat_map = np.vstack((seat_map, l))
            except:
                seat_map = np.append(seat_map, l)

print(seat_map)
'''
SIMULTANOUSLY FOR EACH!!!!!!!! <<< I wasted hours because of this fucking detail.
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
'''

# Make borders by padding to avoid index out-of-range during iteration.
seat_map = np.pad(seat_map, 1, constant_values='0')
y_max = seat_map.shape[0] - 1
x_max = seat_map.shape[1] - 1

f = True
# Analyze every seat within borders and apply the rules until nothing changes. 
while f:
    f = False
    taken = 0
    diary = {}
    for idx, seat in np.ndenumerate(seat_map):
        if seat != '0':
            neighbors = [ seat_map[(idx[0], idx[1]+1)],
                        seat_map[(idx[0], idx[1]-1)],
                        seat_map[(idx[0]+1, idx[1])],
                        seat_map[(idx[0]-1, idx[1])],
                        seat_map[(idx[0]-1, idx[1]-1)],
                        seat_map[(idx[0]+1, idx[1]+1)],
                        seat_map[(idx[0]+1, idx[1]-1)],
                        seat_map[(idx[0]-1, idx[1]+1)] ]
            if seat == 'L':
                if '#' not in neighbors:
                    diary[idx] = '#'
                    f = True
            elif seat == '#':
                taken += 1
                i = 0
                for n in neighbors:
                    if n == '#':
                        i += 1
                if i >= 4:
                    diary[idx] = 'L'
                    f = True
    # "Nastepuje zwolnienie blokady."
    for idx, change in diary.items():
        seat_map[idx] = change

print(taken)
print(seat_map)
