# Linear Algebra Coding the Matrix
# Lab 0.6: Python-- modules and control structures-- and inverse index


#Task 0.6.1: Import the math module using the command
# import math modules
# use math module to perform computations

# import math

# math.sqrt(3)**2
# note this does not return 3 exactly

# cosine of pi
# math.cos(math.pi)

# natural log of e
# math.log(math.e)


# Task 0.6.2: The module random defines a procedure randint(a,b) that returns an integer chosen uniformly at random from among {a, a + 1,...,b}. Import this procedure using
# the command
# >>> from random import randint
# Try calling randint a few times. Then write a one-line procedure movie review(name)
# that takes as argument a string naming a movie, and returns a string review selected
# uniformly at random from among two or more alternatives (Suggestions: “See it!”, “A
# gem!”, “Ideological claptrap!”)

# from random import randint
# def movie_review(name): return ['See it!', 'A gem!', 'Ideological claptrap!'][randint(0,2)]

# Task 0.6.3: In Tasks 0.5.30 and 0.5.31 of Lab 0.5, you wrote procedures
# dict2list(dct, keylist) and list2dict(L, keylist). Download the file dictutil.py
# from http://resources.codingthematrix.com. (That site hosts support code and sample data for the problems in this book.) Edit the provided file dictutil.py and edit it,
# replacing each occurence of pass with the appropriate statement. Import this module, and
# test the procedures. We will have occasion to use this module in the future

# see dictutil.py


# Task 0.6.4: Edit dictutil.py. Define a procedure listrange2dict(L) with this spec:
# • input: a list L
# • output: a dictionary that, for i = 0, 1, 2,..., len(L) 

# see dictutil.py

# Task 0.6.5: Type the above for-loop into Python. You will see that, after you enter the
# first line, Python prints an ellipsis (...) to indicate that it is expecting an indented block of
# statements. Type a space or two before entering the next line. Python will again print the
# ellipsis. Type a space or two (same number of spaces as before) and enter the next line.
# Once again Python will print an ellipsis. Press enter, and Python should execute the loop

# Completed in python command line. For loop in inverse dictionary lab file 


# Task 0.6.6: Write a procedure makeInverseIndex(strlist) that, given a list of strings
# (documents), returns a dictionary that maps each word to the set consisting of the document
# numbers of documents in which that word appears. This dictionary is called an inverse index.
#Hint: use enumerate.

#split strings
#def makeInverseIndex(strlist):
    # strlist contains a list of docs. each doc contains strings
    # split each document into a list of individual strings
#    doc_strings = [i.split() for i in strlist ]
    
    # create set of unique strings across all docs. 
    # use of sum() here puts strings into a single list
#    all_strings = set(sum(doc_strings,[]))
    
    # enumerate docs
#    enumerated_docs = list(enumerate(doc_strings)
    
    #create (doc #, string) tuples containing doc number for each string instance
#    doc_tuples = [(i,j[k]) for (i,j) in enumerated_docs for k in range(len(doc_strings[i]))]
    
    # iterate over tuples and bind string (key) to all docs in which it appears (value)
#    Inverse_index ={i:{j for (j,k) in doc_tuples if k==i} for i in all_strings}
#    return Inverse_index 
 

### CODE BELOW WAS USED TO WRITE ABOVE PROCEDURE
 
# test doc
# acts as strlist above
#docs = ['I like', 'I like to', 'I like to move it', 'I like to move it move it']

# enumerate docs
#enumerated_docs = list(enumerate(docs))
# splits each doc into list of strings; each element in list is a doc
#doc_strings = [i.split() for i in docs]

# set of all words in docs
# recall that passing [] as an argument to sum allows us to put elements into a single list
#all_strings = set(sum(doc_strings,[]))

# iterates over all strings and doc lists
# checks for match within each doc and pairs string to sets of docs where it appears
# this works but is wild and inefficient. . .
#{ i:{enumerated_docs[k][0] for k in range(len(enumerated_docs)) 
#if any(i in x for x in enumerated_docs[k][1])} for i in all_strings} 

