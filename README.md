# Inductive Program Synthesis

Programming by Example (PBE) is the process of generating a program from a set of input-output pairs (or examples). In PBE, the goal is learn a program that can generalize from the given examples and produce correct outputs for inputs not seen before.

In this recitation, you are going to synthesize two simple function using Z3, an SMT (Satisfiability Modulo Theories) solver. 
Given a set of input-output pairs, your goal is to construct a Z3 formula that represents the constraints imposed by these examples. The Z3 solver will then attempt to find a solution that satisfies all of the constraints. The solution to the formula corresponds to a function that satisfies the input-output pairs.

To accomplish this, you will need to create Z3 variables and expressions that represent the possible operations, and use them to construct constraints based on the input-output pairs.


## Set up

Make a fork of this repository.

## Create a Python virtual environment
First, create a virtual environment to isolate the dependencies:
```
python3 -m venv venv
```
Then activate the virtual environment:
```
source venv/bin/activate
```
## Install z3-solver
Install the Z3 solver Python interface:
```
pip install z3-solver
```
## Question 1

### Function Specification:

The function will take two ORDERED inputs, and produces an output. Based on magic intuition, we know the following about the function:
1. It only uses the operations * and <<
2. It returns the result of a single statement of the form
    `f(x, y) = x <OP> y` or `f(x, y) = y <OP> x`.
3. It uses both inputs, but you do not know in what order.

### Function IO Pairs:
```
   IN: (3, 5)    OUT: 40  
   IN: (6, 9)    OUT: 576  
   IN: (23, 44)  OUT: 369098752  
   IN: (16, 22)  OUT: 1441792  
   IN: (8, 9)    OUT: 2304  
```
From the given IO pairs, you may already be able to tell what the function should be,
but we can still formulate this as a synthesis problem and use Z3 to solve it. This technique
will become especially helpful for dealing with more complicated functions (i.e. like the one you will synthesize in HW7). 

You can use the template in `ex1.py` to help you get started!

The main steps of the synthesis process are as follows:

- Define Z3 variables and expressions for the possible operations.
- Add a constraints to only allow one operation to be part of the solution.
- Add constraints for each input-output pair.
- Solve the Z3 formula to synthesize the function.


## Question 2

### Function Specification:

The function will take three ORDERED inputs and produces an output. Based on magic intuition, we know the following about the function:

1. It only uses the operations * and <<.
2. It the function is of the form `(x <OP> y) <OP> z` where `[x, y, z]` is some permutation of the three inputs.
3. It uses all inputs, but you do not know in what order.

You can use the template in `ex2.py` to help you get started!


### Function IO Pairs:
```
   IN: (3, 5, 2)    OUT: 192  
   IN: (6, 9, 3)    OUT: 9216  
   IN: (23, 1, 1)   OUT: 46  
   IN: (16, 6, 5)   OUT: 5120  
   IN: (8, 9, 1)    OUT: 4096  
```


# Resources

- [Python Z3 examples](http://ericpony.github.io/z3py-tutorial/guide-examples.htm)
- [Python API](http://z3prover.github.io/api/html/namespacez3py.html)
- [Programming Z3, a guide](http://theory.stanford.edu/~nikolaj/programmingz3.html)
