# Problems from Chapter 3: The Vector Space

from GF2 import one
from vec import Vec
from vecutil import zero_vec

### Vectors in Containers ###

# Problem 3.8.1

# Part 1. Write and test a procedure vec_select using a comprehension with specs:
# input: a list veclist of vectors over the same domain, and an element k of the domain
# output: the sublist of veclist consisting of vectors from v list such that v[k] = 0


def vec_select(veclist, k): return [v for v in veclist if v[k] == 0]

test_vecs = [Vec({'a','b','c', 'd'},{'a':2,'c':1,'d':3}),
             Vec({'a','b','c', 'd'},{'a':3,'b':1,'d':4}),
             Vec({'a','b','c', 'd'},{'a':-1,'b':2,'c':2,'d':0}),
             Vec({'a','b','c', 'd'},{'b':2,'c':2,'d':1})]

# # testing procedure
# print(vec_select(test_vecs,'d'))
# print(vec_select(test_vecs,'a'))


# Part 2. Write and test a procedure vec_sum using the built in procedure sum() with the specs:
# input: a list veclist of vectors and a set D that is their  common domain
# output: the vector sum of the vectors in veclist
# Note the procedure must work if veclist is empty
# Hint-- use the second argument of the sum() function
# Disclaimer-- the sum() function is defined such that for a vec , 0 + v = v. Hence sum() works correctly
# for vectors as long as the list is not empty.
# empty set returns 0 vector?

def vec_sum(veclist, D): return sum(veclist,zero_vec(D))
        # set second sum argument to zero vector in order to return 0 vector when veclist is empty

# testing

# print(vec_sum(test_vecs,{'a','b','c','d'}))
# print(vec_sum([],{'a','b','c','d'}))


# Part 3. Combine the previous procedures to write a procedure vec_select_sum with the following specs:

# input: a set D, a list veclist of vectors with Domain D, and an element k of the domain
# output: the sum of all vectors v in veclist where v[k] = 0

def vec_select_sum(D, veclist, k):
    vecs_with_0 = vec_select(veclist,k) # select vectors containing 0 in kth index
    return vec_sum(vecs_with_0,D)       # sums the vectors

# testing

test_vecs1 = [Vec({'a','b','c', 'd'},{'a':2,'c':1,'d':3}),
             Vec({'a','b','c', 'd'},{'a':3,'b':1,'d':4}),
             Vec({'a','b','c', 'd'},{'a':-1,'b':0,'c':2,'d':0}),
             Vec({'a','b','c', 'd'},{'b':2,'c':2,}),
             Vec({'a','b','c', 'd'},{'a':0,'b':2,'c':2,'d':2})]

# print(vec_select_sum({'a','b','c','d'},test_vecs1,'a'))
# print(vec_select_sum({'a','b','c','d'}, test_vecs1,'d'))
# print(vec_select_sum({'a','b','c','d'},[],'a'))


# Problem 3.8.2 Write and test a procedure scale_vecs(vecdict) with the follow specs
# input: a dictionary vecdict mapping positive numbers to vectors (instances of Vec)
# output: a list of vectors, one for each item of vecdict. If vecdict contains a key k, mapping to a vector v
# the output should contain the vector (1/k)v

def scale_vecs(vecdict):
    return [(1/k)*v for (k,v) in vecdict.items()] # k = key, v = value

#testing

# test_keys = [1,3,-1, 2,4]
# test_vecdict = {i:j for (i,j) in zip(test_keys,test_vecs1)}
# print(test_vecdict)
# [print(scale_vecs(test_vecdict)[i]) for i in range(2)] # print first two vectors


### Linear Combinations ###

#Constructing the span of vectors over GF2

# Problem 3.8.3: Write a procedure GF2_span with the following spec
# input: a set D of labels and a list l of vectors over GF2 with label-set D
# output: list of all linear combos of the vectors in D

def GF2_span(D, L):
    if L == []:
        return zero_vec(D)
    import itertools
    num_vecs = len(L)
    coefs = list(itertools.product([0, one], repeat = num_vecs)) # all possible coefficients (tuples with 0 or one)
    coef_vec_zip = [zip(i,L) for i in coefs] # zips each set of coefficient in coefs with vecs in L
    return [sum([(scalar*vector) for (scalar,vector) in coef_vec_zip[i]]) for i in range(len(coef_vec_zip))]


#testing

GF2_vecs = [Vec({'a','b'},{'a':one}),
             Vec({'a','b'},{'b':one})]

GF2_vecs1 = [Vec({'a','b','c'},{'a':one, 'b':one}),
             Vec({'a','b','c'},{'a':one,'c':one}),
             Vec({'a','b','c'},{'b':one,'c':one})]

# print(GF2_span({'a','b'},GF2_vecs))
# print(GF2_span({'a','b'},[]))
# print(GF2_span({'a','b'},GF2_vecs1))