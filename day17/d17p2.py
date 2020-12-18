''''
--- Part Two ---
For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....
After the full six-cycle boot process completes, 848 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left in the active state after the sixth cycle?

'''

inp = """##..#.#.
#####.##
#######.
#..#..#.
#.#...##
..#....#
....#..#
..##.#.."""

import numpy as np

# Prepare the matrix representing the pocket dimension.
pd = np.array(list(range(8))) 
arr = inp.split()
for s in arr:
    pd = np.vstack((pd, list(s)))
pd = np.delete(pd, 0, 0)
pd = np.reshape(pd, (1, 1, 8, 8))
pd = np.pad(pd, 1)
print(pd)
# Implement the concept of neighbors and harvesting their state.
def get_neighbor_states(matrix, index):
    states = {}
    operations = (-1, +0, +1)
    # 81 is the quantity of possible variations - 3^4.
    while len(states) < 81:
        i = 0
        for o1 in operations:
            for o2 in operations:
                for o3 in operations:
                    for o4 in operations:
                        iv = (index[0] + o1, index[1] + o2, index[2] + o3, index[3] + o4)
                        states[iv] = ''
    del states[index]

    for cord in states.keys():
        states[cord] = matrix[cord]

    return states

# Implement the logic of cube behavior. 
def evaluate_state(state, neighbors):
    active = list(neighbors.values()).count('#')
    if state == '#':
        if active == 2 or active == 3:
            return state
        else:
            return '.'
    elif state == '.':
        if active == 3:
            return '#'
        else:
            return '.'

# Pocket dimension is infinite. Expand the 'vision' before a cycle. 
def expand_view(matrix):
    matrix = matrix[1:-1, 1:-1, 1:-1, 1:-1]
    matrix = np.pad(matrix, 1, constant_values = '.')
    matrix = np.pad(matrix, 1)
    return matrix

# Collect data about cube states and corresponding transformations.
def harvest_cubes(matrix):
    record = {}
    matrix = expand_view(matrix)
    # considered coordinates:
    c_timexd = range(1, matrix.shape[0] - 1)
    c_layers = range(1, matrix.shape[1] - 1)
    c_columns = range(1, matrix.shape[3] - 1) 
    c_rows = range(1, matrix.shape[2] - 1)
    for w in c_timexd:
        for z in c_layers:
            for y in c_rows:
                for x in c_columns:
                   record[(w, z, y, x)] = evaluate_state(matrix[w, z, y, x], get_neighbor_states(matrix, (w, z, y, x)))
    return matrix, record

# Run the cycle
def cycle_flush(matrix, count):
    matrix, changes = harvest_cubes(matrix)
    for cord in changes.keys():
        matrix[cord] = changes[cord]
        if changes[cord] == '#':
            count += 1
    return matrix, count

i = 0
counter = 0
while i < 6:
    pd, counter = cycle_flush(pd, 0)
    i += 1

print(counter)
