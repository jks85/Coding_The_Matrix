import matutil
from matutil import mat2coldict, mat2rowdict, listlist2mat, coldict2mat, rowdict2mat
from vecutil import list2vec
from vec import Vec
from mat import Mat

# Matrix-vector and vector-matrix multiplication procedures
# In this assignment we write alternative vector/matrix multiplication procedures using the matutil module
# Cannot use the multiplication procedures defined in the Mat class
# Do not exploit sparsity

# Problem #4.17.13 Write the procedure lin_comb_mat_vec_mult(M,v), which multiplies M and v using the linear combination
# definition. For this problem the only operation allowed on v is to select an entr using brackets, e.g. v[k]. The vector
# returned must be computed as a linear combination.

# M*v treats multiplication as a linear combination of the columns of M, weighted by the entries of v

def lin_comb_mat_vec_mult(M,v):

    assert M.D[1] == v.D
    M_cols = mat2coldict(M) # convert columns of M to vecs
    return sum([v[i]*M_cols[i] for i in range(len(v.D))]) # multiply each col by corresponding entry of v and return sum

# used matrix and vector below to test procedure
A = listlist2mat([[-1,1,2],[1,2,3],[2,2,1]])
v = list2vec([1,2,0])
print(lin_comb_mat_vec_mult(A,v))


# Problem #4.17.14 Write the procedure lin_comb_vec_mat_mult(v,M), which multiplies v and M using the linear combination
# definition. For this problem the only operation allowed on v is to select an entr using brackets, e.g. v[k]. The vector
# returned must be computed as a linear combination.

# v*M treats multiplication as a linear combination of the rows of M, weighted by the entries of v

def lin_comb_vec_mat_mult(v,M):
    assert v.D == M.D[0]
    M_rows = mat2rowdict(M) # convert rows of M to dict of vecs
    return sum([v[i]*M_rows[i] for i in range(len(v.D))])

# test procedure on vec and mat below
w = list2vec([4,3,2,1])
B = listlist2mat([[-5,10],[-4,8],[-3,6],[-2,4]])
print(lin_comb_vec_mat_mult(w,B))


# Problem #4.17.15 Write the procedure dot_product_mat_vec_mult(M,v), which multiplies M and v using the dot-product
# definition. For this problem the only operation allowed on v is taking the dot-product of v and another vector u .
# The entries of the vector returned must be computed using dot-product

# Treat M*v as dot-product of rows in M with v. ith row of M dotted with v gives ith entry of resulting vector

def dot_product_mat_vec_mult(M,v):
    assert M.D[1] == v.D
    M_rows = mat2rowdict(M) # convert matrix M to dict of row vectors
    return Vec(M.D[0],{k:(row*v) for (k,row) in M_rows.items()}) # dot row vector with v, assign to corresponding entry


# used matrix and vector below to test procedure
A = listlist2mat([[-1,1,2],[1,2,3],[2,2,1]])
v = list2vec([1,2,0])
print(dot_product_mat_vec_mult(A,v))


# Problem #4.17.16 Write the procedure dot_product_vec_mat_mult(v,M), which multiplies v and M using the dot-product
# definition. For this problem the only operation allowed on v is taking the dot-product of v and another vector u .
# The entries of the vector returned must be computed using dot-product

# Treat v*M as dot-product of v with columns of M. v dotted with ith col of M dotted ith entry of resulting vector.

def dot_product_vec_mat_mult(v,M):
    assert v.D == M.D[0]
    M_cols = mat2coldict(M) # convert matrix M to dict of column vectors
    return Vec(M.D[1],{k:(v*col) for (k,col) in M_cols.items()}) # dot v and col, assign to corresponding entry

# test procedure on vec and mat below
w = list2vec([4,3,2,1])
B = listlist2mat([[-5,10],[-4,8],[-3,6],[-2,4]])
print(dot_product_vec_mat_mult(w,B))

# Matrix-matrix multiplication procedures
# In this assignment we write several matrix/matrix multiplication procedures using specified definitions of matrix
# multiplication.
# Cannot use the multiplication procedures defined in the Mat class
# Use matutil module
# Do not exploit sparsity

# Problem 4.17.17 Write Mv_mat_mat_mult(A,B) to compute the matrix-matrix multiplication of A*B using the matrix-vector
# multiplication definition of matrix-matrix multiplication. For this procedure the only allowed operation on A is to
# perform matrix-vector multiplication with A using A*v.
# Do not use the matrix_vector_mul() or any procedures defined previously

# A*B using mat-vec multiplication. ith column of resulting matrix is A*b_i where b_i is ith column of B

def Mv_mat_mat_mult(A,B):
    assert A.D[1] == B.D[0]
    B_cols = mat2coldict(B) # convert B to dict of column vectors
    col_vecs = {i:A*b for (i,b) in B_cols.items()} # multiply A by each column and place in a dict
    return coldict2mat(col_vecs)

# test procedure on examples below

A = listlist2mat([[-1,1,2],[1,2,3],[2,2,1]])
V = Mat.transpose(matutil.listlist2mat([[1,2,0]]))
print(Mv_mat_mat_mult(A,V))

W = matutil.listlist2mat([[4,3,2,1]])
B = listlist2mat([[-5,10],[-4,8],[-3,6],[-2,4]])
print(Mv_mat_mat_mult(W,B))


# Problem 4.17.18 Write vM_mat_mat_mult(A,B) to compute the matrix-matrix multiplication of A*B using the vector-matrix
# multiplication definition of matrix-matrix multiplication. For this procedure the only allowed operation on A is to
# perform vector-matrix multiplication with A using v*A.
# Do not use the vector_matrix_mul() or any procedures defined previously

# A*B using vec-mat multiplication. ith row of resulting matrix is a_i*B where a_i is ith row of A

def vM_mat_mat_mult(A,B):
    assert A.D[1] == B.D[0]
    A_rows = mat2rowdict(A)
    row_vecs = {i:a*B for (i,a) in A_rows.items()}
    return rowdict2mat(row_vecs)

# test procedure on examples below
print('vM_mat_mat test below')
A = listlist2mat([[-1,1,2],[1,2,3],[2,2,1]])
V = Mat.transpose(matutil.listlist2mat([[1,2,0]]))
print(vM_mat_mat_mult(A,V))

W = matutil.listlist2mat([[4,3,2,1]])
B = listlist2mat([[-5,10],[-4,8],[-3,6],[-2,4]])
print(vM_mat_mat_mult(W,B))


# 4.17.19 Let A be a matrix whose column labels are countries and whose row labels are votes taken in the United Nations,
# where A[i,j] is +1 (yes), -1 (no), or 0 (neither) indicating how country j voted on vote i.

# The entries of A^T*A contain dot products of countries voting records as in the Voting Lab. Read in the data, create
# the matrix A, and matrix M.
# note that the final entry of each vote string contains a '\n'

voting_data = open('UN_voting_data.txt') # read file of voting data
UN_votes= list(voting_data) # create list. note last element in each string is '\n' which needs to be removed

split_records = [y.split('\n') for y in UN_votes] # separate '\n' at end of string
raw_records = [rec[0].split(' ') for rec in split_records] # create list of lists containing country name and votes
countries = {z[0] for z in raw_records} # create country labels
vote_numbers = {i+1 for i in range(len(raw_records[0])-1)} # create labels for vote numbers (1st vote, 2nd vote, etc)

# voting_dict below creates a dictionary (vote_number, country):vote by iterating over records
# exploits sparsity (see filter)
# converts -1's and 1's from strings into ints
voting_dict = {(i,rec[0]):int(rec[i]) for rec in raw_records #
               for i in range(len(rec))if rec[i] == '1' or rec[i] == '-1'}

# create matrices to analyze voting patterns

A = Mat((vote_numbers,countries),voting_dict) # create matrix of voting record by country
A_T = A.transpose() # create transpose

# note matrix multiplication below takes some time to complete. don't run carelessly...


# M = A_T*A  # entries of matrix product are dot-products of voting records

# Line above is commented out b/c my computer is not powerful enough to compute M in a reasonable amount of time.I have
# skipped the computational questions related to using M to analyze votes

# Comprehension Practice

# Problem 4.17.20 Write the one line procedure dictlist_helper(dlist,k) with the following spec:
# input a list dlist of dictionaries which all have the same keys, and a key k
# output: the list whose ith element is the value corresponding to key k in the ith dictionary of dlist

def dictlist_helper(dlist,k):
    return [dict[k] if k in dict.keys() else 'invalid key' for dict in dlist] # return values or error if key is invalid



