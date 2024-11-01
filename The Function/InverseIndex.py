# Task 0.6.6: Write a procedure makeInverseIndex(strlist) that, given a list of strings
#(documents), returns a dictionary that maps each word to the set consisting of the document
# numbers of documents in which that word appears. This dictionary is called an inverse index.
# (Hint: use enumerate.)

def makeInverseIndex(strlist):
    # strlist contains a list of docs. each doc contains strings
    # split each document into a list of individual strings
    doc_strings = [i.split() for i in strlist ]
    
    # create set of unique strings across all docs. 
    # use of sum() here puts strings into a single list
    # use of set() constructor removes repeat strings
    all_strings = set(sum(doc_strings,[]))
    
    # enumerate docs
    enumerated_docs = list(enumerate(doc_strings))
    
    #create (doc #, string) tuples containing doc number for each string instance
    doc_tuples = [(i,j[k]) for (i,j) in enumerated_docs for k in range(len(doc_strings[i]))]
    
    # iterate over tuples and bind string (key) to all docs in which it appears (value)
    Inverse_index ={i:{j for (j,k) in doc_tuples if k==i} for i in all_strings}
    return Inverse_index 
    
    
    
# Task 0.6.7: Write a procedure orSearch(inverseIndex, query) which takes an inverse index and a list of words query, and returns the set of document numbers specifying
# all documents that contain any of the words in query


def orSearch( inverseIndex, query):
    # run inverseIndex on each word in query and get list of docs
    query_docs = [inverseIndex[i] for i in query]
    
    # get docs where *any* word appears by taking union of all sets
    return set.union(*query_docs)
    
    
# Task 0.6.8: Write a procedure andSearch(inverseIndex, query) which takes an inverse index and a list of words query, and returns the set of document numbers specifying
# all documents that contain all of the words in query.

def andSearch( inverseIndex, query):
    # run inverseIndex on each word in query and get list of docs
    query_docs = [ inverseIndex[i] for i in query]

    # get docs where *all* words appear by taking intersection of all sets
    return set.intersection(*query_docs)