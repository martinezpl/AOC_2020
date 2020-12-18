'''
--- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###
Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......
After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?
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
pd = np.reshape(pd, (1, 8, 8))
pd = np.pad(pd, 1)
print(pd)
# Implement the concept of neighbors and harvesting their state.
def get_neighbor_states(matrix, index):
    states = {}
    operations = (-1, +0, +1)
    # 27 is the quantity of possible variations - 3^3.
    while len(states) < 27:
        i = 0
        for o1 in operations:
            for o2 in operations:
                for o3 in operations:
                    iv = (index[0] + o1, index[1] + o2, index[2] + o3)
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
    matrix = matrix[1:-1, 1:-1, 1:-1]
    matrix = np.pad(matrix, ((1, 1),(1,1),(1,1)), constant_values = '.')
    matrix = np.pad(matrix, 1)
    return matrix

# Collect data about cube states and corresponding transformations.
def harvest_cubes(matrix):
    record = {}
    matrix = expand_view(matrix)
    # considered coordinates:
    c_layers = range(1, matrix.shape[0] - 1)
    c_columns = range(1, matrix.shape[2] - 1) 
    c_rows = range(1, matrix.shape[1] - 1)
    for z in c_layers:
        for y in c_rows:
            for x in c_columns:
               record[(z, y, x)] = evaluate_state(matrix[z, y, x], get_neighbor_states(matrix, (z, y, x)))
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
