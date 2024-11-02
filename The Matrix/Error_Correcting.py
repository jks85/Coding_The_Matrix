# Lab 4.14: Error Correcting Codes; Linear Algebra Coding the Matrix, Ed. 1

from GF2 import one


import matutil
import vecutil
import bitutil
from mat import Mat
from matutil import mat2coldict
from vec import Vec

# bit strings are encoded and codewords are vectors in GF2.
# There is a linear transformation H such that the vector space of codewords C is the Null(H).
# we can also create the vector space of codewords via "generators". See textbook for example of generator matrix

# 4.14.3 Hamming's Code

# Task 4.14.1: Create an instance of Mat representing the generator matrix G (from the textbook) Use matutil module.

G = matutil.listlist2mat([[one,0,one,one],[one,one,0,one],[0,0,0,one], # converts lists of lists to a matrix
                          [one,one,one,0],[0,0,one,0],[0,one,0,0],[one,0,0,0]]) # each sublist becomes a row
print('matrix G printed below')
print(G)

# Note: column space of G spans set of codewords
# row space of G spans 4 bit strings in GF2 (rows of G contain standard basis 4-vectors in GF2 and linear combos)


# Task 4.14.2: What is the encoding of the message [1,0,0,1]?

p = vecutil.list2vec([one,0,0,one]) # p = [1,0,0,1] in GF2. this is original bit string
print('original bitstring p printed below')
print(p)
c = G*p # encode bitstring via matrix multiplication
print('encoded bit c printed below')
print(c)

# c = [0,0,1,1,0,0,1] in GF2


# 4.14.4 Decoding

# Below are some notes answering conceptual questions from the assignment. code begins with task 4.14.3

# Note that four of the rows in G are standard basis vectors e1, e2, e3, e4 in GF2. What does that imply about
# relationships between words and codewords? Can you easily decode the codeword [0,one,one,one,one,0,0] without
# using a computer?

# Yes, because the transformation matrix G includes the 4 basis vectors in the rows, the image contains the original
# bits mapped to (possibly) new positions. Other positions contain linear combos of original bits

# in G row 2 (note index starts at 0) is e4, row 4 is e3, row 5 is e2, row 6 is e1
# encoding maps 4th digit (not index) into index 2 (3rd slot)
# encoding maps 3rd digit into index 4
# encoding maps 2nd digit into index 5
# encoding maps 1st digit into index 6 (last slot)

# so in a codeword...
# index 2 is 4th digit, index 4 is 3rd digit, index 5 is 2nd digit, index 6 is 1st digit

# Therefore codeword: [0,one,one,one,one,0,0] was encoded from
# [0,0,one,one]


# Task 4.14.3 Construct a 4x7 matrix R such that for any codeword c, the matrix vector product of
# R*c = p, where p is the binary string such that G*p = c (i.e. the unencoded bit string)

# R is the "inverse" of G. Not a true inverse since G is not square (i.e. R is not unique)
# R takes a codeword, 7-vector in GF2 and returns the original string a 4 vector in GF2
# reverse mappings from above....
# digit in index 6 of c maps to index 0 of p (first slot)
# digit in index 5 of c maps to index 1 of p (second slot)
# digit in index 4 of c maps to index 2 of p (third slot)
# digit in index 2 of c maps to index 3 of p ( 4th digit)

# Written as a list of lists (each sublist is a row)
# R =[[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,0,1,0,0,0,0]]

R = matutil.listlist2mat([[0,0,0,0,0,0,one],[0,0,0,0,0,one,0],[0,0,0,0,one,0,0],[0,0,one,0,0,0,0]])
print('matrix R printed below')
print(R)

print('is R*G == I ?')
print(R*G == matutil.identity({0,1,2,3},one)) # R*G should give 4x4 identity. R is a pseudoinverse
# returns true

print('matrix R*G printed below')
print(R*G)

# 4.14.5 Error Syndrome

# Below are some answers to conceptual questions. Code starts with task 4.14.4.

# let c* represent the codeword after passing through the channel (i.e. errors may be introduced)
# c* is in the column space of G

# c* = c + e; e is an error vector. 1's in corrupted positions

# Task 4.14.4: Create an instance of Mat representing the check matrix H

# note columns of H are binary digits 1 through 7
# if there is one error in e (i.e. a 1), H*e will return the column referencing the position/index of the error
# H*c = 0 for any codeword
# since column space of G spans all codewords H*G = 0 (0 matrix)

H = Mat(({0,1,2},{0,1,2,3,4,5,6}), {(0,0):0, (0,1):0,(0,2):0,(0,3):one,(0,4):one,(0,5):one,(0,6):one,
        (1,0):0, (1,1):one,(1,2):one,(1,3):0,(1,4):0,(1,5):one,(1,6):one,
                                    (2,0):one,(2,1):0,(2,2):one,(2,3):0,(2,4):one,(2,5):0,(2,6):one})

print('product of H*G is below')
print(H*G)
print(' the product of H*G is the 0 matrix as expected')


# 4.14.6 Finding the error

# Note we assume at most 1 error
# if bit i is corrupted in the encoded bit e, then H*e returns column i
# column i can be treated as sa binary number

# error syndrome is es, es = H*e
# gives the location of the error (i.e. the 'one') as a binary string (e.g. 011 means error in position 3)
# error vector has 1 nonzero entry since we have assumed at most one error


# Tasking 4.14.5 Write a procedure find_error that takes an error syndrome and returns the error vector e
# note-- use sparsity!!!

# (we are working backwards)
# es is a column from H indicating the error position as a binary number (e.g. 011 is col 3 of H, so error is in position 3)
# the procedure find_error() converts the binary number to a base 10 number and reconstructs the error vector
# note this procedure assumes the vector is over GF2

def find_error(es):    # es will be of form Vec({0,1,2},{0:__ ,1:__, 2__}) where __ is 0 or one in GF2
    # es in a 3-vec in GF2
    swap_ones = Vec(es.D, {key:1 for (key,val) in es.f.items() if val == one}) # switch instances of one to 1
    slot = sum([2**abs(2-i)*swap_ones[i] for i in swap_ones.D]) # convert binary number for error to base 10; gives error position
    slot = slot -1  # adjust slot to index in error vector
    return Vec({0,1,2,3,4,5,6},{slot:'one'}) # create error vector, which has a 'one' in the position "slot"


print('error syndrome vec below')
test_es = Vec({0, 1, 2},{0: 1, 1: 1, 2: 1})
print(test_es)

print('error vec below')
print(find_error(Vec({0, 1, 2},{0:one, 1:one, 2:one})))

# Task 4.14.6: Bob receives non-codeword v = [1,0,1,1,0,1,1]. Derive the original 4 bit message Alice intended to send.

# get error syndrome using H*v = H*e
# use procedure find_error to get error vector to identify the codeword c
# Recall the R matrix, R =[[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,0,1,0,0,0,0]]
# R is the matrix such that R*c = p, where c is the codeword and p is the original string


# matrix multiplications performed by hand (mat class not finished yet)

v = vecutil.list2vec([one,0,one,one,0,one,one]) # convert v to Vec; converted 1 to one
es = H*v # compute error syndrome; note we don't need to convert 1 to one?
# es = [one,one,one] (as list)

err_vec = find_error(es)
print('error syndrome is below')
print(err_vec)

# v = codeword + err_vec, therefore
# codeword c = v + err_vec (subtraction is same as addition in GF2). this switches the bit in the position with the error

c = v + err_vec # compute correct codeword
print('correct encoded bit is below')
print(c)

p = R*c # Multiply R and c to find original string. See tasks 4.14.3
print('original 4 bit is')
print(p)

# p = [0,one,0,one] # original string as list vec

# Task 4.14.7
# Write a one line procedure find_error_matrix with the following spec
# input: a matrix S whose columns are error syndromes
# output: a matrix whose cth column contains the error vector corresponding to column c of S

# procedure converts S to a col dict of error syndromes
# comprehension finds error vector for each error syndrome
# converts list of col error vectors back into a matrix
def find_error_matrix(S): # entries of S are assumed to be in GF2
    return matutil.coldict2mat([find_error(es) for es in mat2coldict(S).values()])

# testing find_error_matrix()

Q = matutil.listlist2mat([[one,one,one],[0,0,one]])
Q = Q.transpose()

es1 = vecutil.list2vec([one,one,one])
print(find_error(es1))
es2 = vecutil.list2vec([0,0,one])
print(find_error(es2))
print(find_error_matrix(Q))