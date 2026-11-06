from z3 import *
from itertools import *

io_pairs = [
   ((3, 5, 2),192),
   ((6, 9, 3),9216),
   ((23, 1, 1),46),  
   ((16, 6, 5),5120),  
   ((8, 9, 1),4096)
]

def formula(pairs):
    constraints = []
    
    # The program looks like this:
    #   z0 := input[0]
    #   z1 := input[1]
    #   z2 := input[2]
    #   z3 := f3(z3_left, z3_right)
    #   z4 := f4(z3, z4_right)
    # where z3_left, z3_right, z4_right are either z0, z1, or z2
    # and f3, f4 are either mul or shl operations
    
    # TODO: Implement the constraints.
    
    # The general strategy is:
    # 1. Implement the structural constraints first (what is z3_left, z3_right, z4_right, f3, and f4).
    #    Use Boolean flags such as z3_left_is_z0, z4_right_is_z1, f3_is_mul, etc.
    # 2. For each input-output pair, create constraints that the output matches the computation 
    #    defined by the structural constraints.
    
    
    return And(constraints)

if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)
