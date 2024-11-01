### Problems 1.7

## Additional practice problems for writing comprehensions and loops

import sys
sys.path.append('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Field')

import os
os.chdir('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Field')

from plotting import plot


## COMPREHENSIONS

# 1.7.1
# procedure my_filter(L,num)
# input list of numbers and an integer
# output list not containing a multiple of the sum
# L =[1,2,4,5,7], num = 2 should return [1,5,7]

def my_filter(L,num): return [i for i in L if i % num != 0]

# print(my_filter([1,2,4,5,7],2))

# 1.7.2
# input list of non-negative integers
# output list of lists: for every element in L, create a list containing 1,2,3,...,x
# L =[1,2,4] outputs [[1],[1,2],[1,2,3,4]]
# L = [0] outputs [[]]

def my_lists(L): return [(x if x ==[] else [i+1 for i in x]) for x in [list(range(y)) for y in L]]
# moved to new line since it is a long line


    # could clean this up by defining variables for the inner comprehensions e.g.
    # list_of_lists = [list(range(y)) for y in L]; creates initial lists that will be transformed
    # list of lists1 = [i+1 for i in x]; lists that need 1 added to each element
# print(my_lists([1,2,3,4]))
# print(my_lists([0]))

# 1.7.3
# input two functions f and g, represented as dictionaries such that g o f composition exists
# output a dictionary representing the composition g o f

def my_function_composition(f,g): return {x:g[f[x]] for x in f.keys()}

# create dicts to test
# note squares and square_dict are set up so that
# the composition always exists when adding 1 then squaring
# for above method f= add 1, g = square
# add_1 = [i+1 for i in range(5)]
# squares = [i*i for i in add_1]
# add_1_dict = {x:y for (x,y) in zip(range(5), add_1)}
# square_dict = {x:y for (x,y) in zip(add_1, squares)}

# print(my_function_composition(add_1_dict,square_dict))

## LOOPS

# 1.7.4
# return the sum of a list of numbers without using sum()
# not 100% sure how python handles the loop execution when list is empty
# but it works. . .

def mySum(L):
#    set initial value to 'empty' if list is empty, otherwise to 0
     current = 'empty list' if L == [] else int()
     for x in L:
         current = current + x
     return current

# print(mySum([1,2,3]))
# print(mySum([]))
#
# # 1.7.5
# # return the product of the numbers in the list
# not 100% sure how python handles the loop execution when list is empty
# but it works. . .


def myProduct(L):
#    set initial value to 'empty' if list is empty, otherwise 1
     current = 'empty list' if L == [] else 1
     for x in L:
         current = current * x
     return current
#
#
# print(myProduct([1,2,3,4]))
# print(myProduct([]))

# 1.7.5
# find the minimum of a list
# not 100% sure how python handles the loop execution when list is empty
# but it works. . .


def myMin(L):
# input list of numbers
# output minimum value in list

# #     # set initial value to empty of L is empty otherwise set to first element
    current = 'empty list' if L == [] else L[0]
    for x in L:
        current = x if x < current else current
        return current
# #
# #
# # print(myMin([3,5,-1]))

# 1.7.7
# input list of strings
# output concatenation of strings in list L

def myConcat(L):

#   set initial value to empty string
    current = ''
    if (L == []):
        return current # return empty string if list is empty
    else:
        for x in L:
            current = current + x
        return current  #return concatenated list otherwise
#
#
# print(myConcat(['ready','set','go']))
# print(myConcat([]))


# 1.7.8
# input: list of sets
# output: union of all sets in L

def myUnion(L):
    if (L == []):
        return 'empty list'
    else:
        current = set()  # initialize empty set
        for x in L:
            current = current | x
        return current


# 1.7.12
# Write a procedure transform(a,b,L) with the following spec:
# input: complex numbers a and b, and a List L of complex numbers
# output: list of complex numbers obtained by applying f(z) = az + b to each number in L

from math import pi, e

def transform(a, b, L):
    return [(a*x + b) for x in L]

# Pick a and b to perform the following transformations (IN ORDER)
# 1. translate z one unit up and one unit right ---> add (1+1j)
# 2. rotate 90 degrees clockwise ---> multiply by -1j
# 3. Scale by 2 ---> multiply by 2

# composition algebraically is
# f(z) = (z + (1+1j))*-1j*2)
# a = -2j
# b = 2-2j