#2.12 Lab: Comparing voting records using dot-product

import os
from venv import create

os.chdir('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Vector')

import sys
sys.path.append('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Vector')

os.listdir()

### putting list dot product procedure in here

def list_dot(u,v): return sum([u[i]*v[i] for i in range(len(u))])



f = open('US_Senate_voting_data_109.txt') # open voting data file
# note that the list of strings has a '\n' at the end for a new line. need to split this out first. . .

voting_records = list(f) # list of string with voting data delimited by spaces " "

voting_string = [i.split(' ') for i in voting_records] # split voting info into list of separate strings

# Task 2.12.1: Write a procedure create_voting_dict(strlist) that takes in a listo f strings (from voting record
# source file) and returns a dictionary mapping the senator's last name to a list containing their voting record

def create_voting_dict(strlist):
    # strlist is a string of vote info delimited by spaces read in from text file
    split_line = [line.split('\n') for line in strlist] # last string needs to have '\n' separated
    voting_data = [split_line[i][0].split(' ') for i in range(len(split_line))] # split voting records by spaces
    sen_name = [x[0] for x in voting_data] # get senator last names (first val in list)
    sen_votes_str = [x[3:] for x in voting_data] # get senator voting data (strings)
    sen_votes = [[int(x) for x in vote_list] for vote_list in sen_votes_str] # convert votes to ints
    vote_dict = {name:vote for (name,vote) in zip(sen_name,sen_votes)}
    return vote_dict


f = open('US_Senate_voting_data_109.txt')
check_votes = list(f)

### VOTE DICTIONARY ###
vote_record = create_voting_dict(check_votes)



# print(vote_record)
# print(type(vote_record['Obama']))

# Task 2.12.2 Write procedure policy_compare(sen_a,sen_b,voting_dict)

def policy_compare(sen_a,sen_b,voting_dict):
    # sen_a and sen_b must be strings of senator last names
    sen_a_votes = voting_dict[sen_a]
    sen_b_votes = voting_dict[sen_b]
    return list_dot(sen_a_votes,sen_b_votes)

#testing procedure
# print(policy_compare('Akaka','Alexander', vote_record))
# returns 11 (min is -46, max is 46)
# print(vote_record.keys())

# Task 2.12.3 Write procedure most_similar(sen,voting_dict) that inputs a senator name and voting dictionary
# and returns the name of the senator who voted most similarly (besides that senator)


def most_similar(sen,voting_dict):
    sen_names = voting_dict.keys() # get list of senator names
    # compare_names = [name for name in sen_names if name != sen] # make list of names removing senator in question
    comparisons =[(name,policy_compare(sen, name, voting_dict)) for name in sen_names if name != sen] # compare senators (name, #)
    comparison_vals = [y for (x,y) in comparisons] # get numerical comparison values
    biggest = max(comparison_vals)  # get max value; this corresponds to most similar senator(s)
    return [x for (x,y) in comparisons if y == biggest] # return name of senator(s) with highest similarity
    # note: hopefully this code returns multiple senators in the case of a tie



# Task 2.12.4 Write procedure least_similar(sen,voting_dict) that inputs a senator name and voting dictionary
# and returns the name of the senator who voted least similarly (besides that senator)

# similar to procedure above but check min stead of max

def least_similar(sen,voting_dict):
    sen_names = voting_dict.keys()  # get list of senator names
    # compare_names = [name for name in sen_names if name != sen] # make list of names removing senator in question
    comparisons = [(name, policy_compare(sen, name,voting_dict)) for name in sen_names if name != sen]  # compare senators (name, #)
    comparison_vals = [y for (x, y) in comparisons]  # get numerical comparison values
    smallest = min(comparison_vals)  # get max value; this corresponds to most similar senator(s)
    return [x for (x, y) in comparisons if y == smallest]  # return name of senator(s) with highest similarity
    # note: hopefully this code returns multiple senators in the case of a tie

# Task 2.12.5: Check the most similar senator to Rhode Island legend Lincoln Chafee
# and the least similar senator to Pennsylvania's Rick Santorum

# print('Chafee is most similar to {}'.format(most_similar('Chafee', vote_record)))
# print('Santorum is least similar to {}'.format(least_similar('Santorum', vote_record)))

# Task 2.12.7: Write a procedure find_average_similarity(sen,sen_set,voting_dict) that given a senator, compares
# that senator's record to the record of all senators in sen_set.
# compare by computing the dot product for each possible pair and return the average
# use this to compare democratic senators with other democratic senators

def find_average_similarity(sen,sen_set,voting_dict):
    from statistics import mean
    comps =[policy_compare(sen, senators, voting_dict) for senators in sen_set] # compare sen to senators in sen_set
    return mean(comps)

# print(find_average_similarity('Obama',['Biden','Chafee'],vote_record))

def get_democrats(strlist):     # get names of democrats from vote records
    # strlist is a string of vote info delimited by spaces read in from voting text file
    split_line = [line.split('\n') for line in strlist]  # last string needs has an '\n'. Separate it
    voting_data = [split_line[i][0].split(' ') for i in range(len(split_line))]  # split voting records by spaces
    sen_name_party = [(x[0],x[1]) for x in voting_data]  # get senator last name and party
    dems = [name for (name, party) in sen_name_party if party == 'D']
    return dems

def get_republicans(strlist):   # get names of republicans from vote records
    # strlist is a string of vote info delimited by spaces read in from voting text file
    split_line = [line.split('\n') for line in strlist]  # last string needs has an '\n'. Separate it
    voting_data = [split_line[i][0].split(' ') for i in range(len(split_line))]  # split voting records by spaces
    sen_name_party = [(x[0],x[1]) for x in voting_data]  # get senator last name and party
    repubs = [name for (name, party) in sen_name_party if party == 'R']
    return repubs

# Check which senator has highest average similarity to democrats and to republicans

dem_list = get_democrats(check_votes)
rep_list = get_republicans(check_votes)
#
# similarity_tuples = [(sen,find_average_similarity(sen, dem_list, vote_record)) for sen in vote_record.keys()]
# similarity_scores_dem = [score for (senator, score) in similarity_tuples]
# max_score_dem = max(similarity_scores_dem)
# min_score_dem = min(similarity_scores_dem)
# most_similar_dem = [senator for (senator, score) in similarity_tuples if score == max_score_dem]
# least_similar_dem = [senator for (senator, score) in similarity_tuples if score == min_score_dem]
# print('{} votes most similarly to the democratic party on average'.format(most_similar_dem))
# print('{} votes least similarly to the democratic party on average'.format(least_similar_dem))
# print(similarity_tuples)
# # print(dem_list)
# # print(rep_list)
#
# similarity_tuples = [(sen,find_average_similarity(sen, rep_list, vote_record)) for sen in vote_record.keys()]
# similarity_scores_rep = [score for (senator, score) in similarity_tuples]
# max_score_rep = max(similarity_scores_rep)
# min_score_rep = min(similarity_scores_rep)
# most_similar_rep = [senator for (senator, score) in similarity_tuples if score == max_score_rep]
# least_similar_rep = [senator for (senator, score) in similarity_tuples if score == min_score_rep]
# print('{} votes most similarly to the republican party member on average'.format(most_similar_rep))
# print('{} votes least similarly to the republican party on average'.format(least_similar_rep))
# print(similarity_tuples)

# Biden had the highest average similarity with the set of democrats


# Task 2.12.8: Write a procedure find_average_record(sen_set,voting_dict) that given a set of senator names
# finds the average voting record

def find_average_record(sen_set,voting_dict):
# find average record by first summing voting vectors then dividing by number of voters
    num_voters = len(sen_set)
    sen_votes = [voting_dict[senator] for senator in sen_set] # make list of lists containing senator votes
    zipped_votes = list(zip(*sen_votes)) # zip votes to make take summation. note use of * operator to unpack list
    sum_votes = [sum(i) for i in zipped_votes]
    average_record = [i/num_voters for i in sum_votes]
    return average_record

# check average record of dem senators
# print(find_average_record(dem_list, vote_record))
average_Democrat_record = find_average_record(dem_list, vote_record)

# check who is most similar to average dem

sim_scores = [(sen,list_dot(average_Democrat_record, vote_record[sen])) for sen in vote_record.keys()] #similarity val
# (name, value) higher value means more similar to average
max_score = max([y for (x,y) in sim_scores])
most_average = [x for (x,y) in sim_scores if y == max_score]
# print('{} votes most similarly to the demoratic senator average'.format(most_average))

# same answer as before which makes sense
# since the dot product is commutative summing the vectors first and then taking the dot product achieves
# the same result as taking all the dot products then summing (original method)

# Task. 2.12.6 Bitter Rivals
# Write a procedure bitter_rivals(voting_dict) that takes a voting dictionary and determines
# which senators disagree the most

def bitter_rivals(voting_dict):
    pairs = [(x,y) for x in voting_dict.keys() for y in voting_dict.keys() if x != y] # all pairs of distinct senators
    pair_sim = [(x,y,list_dot(voting_dict[x],voting_dict[y])) for (x,y) in pairs] # dot product to compute similarity
    sim_scores = [z for (x,y,z) in pair_sim] # collect scores
    min_sim_score = min(sim_scores) # get min scores (most divergent voting pair)
    rivals = [(x,y) for (x,y,z) in pair_sim if z == min_sim_score]
    return rivals

print(bitter_rivals(vote_record))
#Feingold and Inhofe were the most divergent senators

# is McCain a maverick

print(find_average_similarity('McCain',vote_record.keys(),vote_record))
# McCain 23.0 similarity score with all senators

print(find_average_similarity('McCain',rep_list,vote_record))
# McCain 30.5 similarity score with republicans

print(find_average_similarity('McCain',dem_list,vote_record))
# McCain 30.5 similarity score with democrats


# # check similarity for individual republicans vs republican average
# print([(x,find_average_similarity(x,rep_list,vote_record)) for x in rep_list])
# similarity_rep = [(x,find_average_similarity(x,rep_list,vote_record)) for x in rep_list]
# similarity_scores_rep = [y for (x,y) in similarity_rep]
# similarity_rep_min = [(x,y) for (x,y) in similarity_rep if y == min(similarity_scores_rep)]
# similarity_rep_max = [(x,y) for (x,y) in similarity_rep if y == max(similarity_scores_rep)]
# print('The minimum similarity among republicans is from{}'.format(similarity_rep_min))
# print('The maximum similarity among republicans is from{}'.format(similarity_rep_max))

# Maximium similarity republicans are Allen, Bond, Grassley, Roberts, and Talent; score of 39.6 (same as earlier)
# Minimum similarity republicans is Chafee; score of 23.8
# McCain's similarity score appears within the norm but could investigate more


# Is Obama extremist
print(find_average_similarity('Obama',vote_record.keys(),vote_record))
# Obama 25.5 similarity score with all senators

print(find_average_similarity('Obama',dem_list,vote_record))
# Obama 31.7 similarity score with democrats

print(find_average_similarity('Obama',rep_list,vote_record))
# Obama 20.6 similarity with republicans


# Could do more detailed analysis compared to 5 # summary but Obama appears to vote slightly more with Dems
# Than McCain votes with Republicans. Both are well within the norm