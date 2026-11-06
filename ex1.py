from z3 import *

io_pairs = [
    ((3, 5), 40),
    ((6, 9), 576),
    ((23, 44), 369098752),
    ((16, 22), 1441792),
    ((8, 9), 2304),
]

def formula(pairs):
    constraints = []
    
    # There are four possible operations:
    #  1. f(x, y) = x * y
    #  2. f(x, y) = y * x
    #  3. f(x, y) = x << y
    #  4. f(x, y) = y << x
    
    # Use Boolean flags B0, B1, B2, B3 to indicate which operation is used.
    flags = [Bool(f'B{i}') for i in range(4)]
    
    # Constrain that exactly one of the flags is True.
    exactly_one_flag = ... # TODO: Fill in here
    constraints.append(exactly_one_flag)
    
    # For each input-output pair, create a constraint that the output matches one of the possible operations.
    for (x, y), ans in pairs:
        pair_constraint = ... # TODO: Fill in here
        constraints.append(pair_constraint)

    return And(constraints)


if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)
    