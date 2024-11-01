# Copyright 2013 Philip N. Klein

# creates a list of values in dictionary from a dictionary and a keylist
def dict2list(dct, keylist): return [dct[i] for i in keylist]


# creates a dictionary from a list of values and keys
def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist,L)}


#creates a dictionary from a list of values using the list indices as keys
def listrange2dict(L): return {i:L[i] for i in range(len(L))}