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
    # and f3, f4 are either multiplication or left shift operations
    
    # Constrain what z3_left is
    z3_left_is_z0 = Bool('z3_left_is_z0')
    z3_left_is_z1 = Bool('z3_left_is_z1')
    z3_left_is_z2 = Bool('z3_left_is_z2')
    z3_left_is_z = [z3_left_is_z0, z3_left_is_z1, z3_left_is_z2]
    # z3_left is one of the three options
    constraints.append(sum([If(z3_left_is_z[i], 1, 0) for i in range(3)]) == 1)

    # constrain what z3_right is
    z3_right_is_z0 = Bool('z3_right_is_z0')
    z3_right_is_z1 = Bool('z3_right_is_z1')
    z3_right_is_z2 = Bool('z3_right_is_z2')
    z3_right_is_z = [z3_right_is_z0, z3_right_is_z1, z3_right_is_z2]
    # z3_right is one of the three options
    constraints.append(sum([If(z3_right_is_z[i], 1, 0) for i in range(3)]) == 1)

    # constrain what z4_right is
    z4_right_is_z0 = Bool('z4_right_is_z0')
    z4_right_is_z1 = Bool('z4_right_is_z1')
    z4_right_is_z2 = Bool('z4_right_is_z2')
    z4_right_is_z = [z4_right_is_z0, z4_right_is_z1, z4_right_is_z2]
    # z4_right is one of the three options
    constraints.append(sum([If(z4_right_is_z[i], 1, 0) for i in range(3)]) == 1)
    
    # constrain what f3 is (either multiplication or left shift)
    f3_is_mul = Bool('f3_is_mul')
    f3_is_shl = Bool('f3_is_shl')
    f3_is = [f3_is_mul, f3_is_shl]
    # f3 is one of the two options
    constraints.append(sum([If(f3_is[i], 1, 0) for i in range(2)]) == 1)
    
    # constrain what f4 is (either multiplication or left shift)
    f4_is_mul = Bool('f4_is_mul')
    f4_is_shl = Bool('f4_is_shl')
    f4_is = [f4_is_mul, f4_is_shl]
    # f4 is one of the two options
    constraints.append(sum([If(f4_is[i], 1, 0) for i in range(2)]) == 1)
    
    
    for i, (inputs, output) in enumerate(pairs):
        z0 = BitVec(f'z0_{i}', 16)
        z1 = BitVec(f'z1_{i}', 16)
        z2 = BitVec(f'z2_{i}', 16)
        input_constr = And(z0 == inputs[0], z1 == inputs[1], z2 == inputs[2])
        constraints.append(input_constr)
        
        z3_left = If(z3_left_is_z0, z0, If(z3_left_is_z1, z1, z2))
        z3_right = If(z3_right_is_z0, z0, If(z3_right_is_z1, z1, z2))
        z3 = If(f3_is_mul, z3_left * z3_right, z3_left << z3_right)
        
        z4_right = If(z4_right_is_z0, z0, If(z4_right_is_z1, z1, z2))
        z4 = If(f4_is_mul, z3 * z4_right, z3 << z4_right)
        constraints.append(z4 == output)
    
    return And(constraints)

if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)
