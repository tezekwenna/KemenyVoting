# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 01:59:51 2016

@author: tobez
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import prefpy

def plurality(preferences):
    x = {}
    for vote in preferences:
        x[vote[0]] = x.get(vote[0], 0) + 1
    return sorted(x.items(), key = lambda y: y[1], reverse = True)

def borda(preferences):
    x = {}
    scores = range(len(preferences[0]) - 1, -1, -1)
    for vote in preferences:
        #for i in range(len(vote) - 1, -1, -1):
        for cand, score in zip(vote, scores):
            x[cand] = x.get(cand, 0) + score
    return sorted(x.items(), key = lambda y: y[1], reverse = True)

def veto(preferences):
    x = {}
    scores = range(len(preferences[0]) - 1, -1, -1)
    for vote in preferences:
        #for i in range(len(vote) - 1, -1, -1):
        for cand, score in zip(vote, scores):
            x[cand] = x.get(cand, 0) + score
    return sorted(x.items(), key = lambda y: y[1], reverse = True)

def weightedMajorityGraph(preferences):
    comps = {}
    for vote in preferences:
        for i in range(len(vote)):
            for j in range(i + 1, len(vote)):
                comps[(vote[i], vote[j])] = comps.get((vote[i], vote[j]), 0) + 1
    return comps
        #for cand1, cand2 in zip(vote, vote[1:])       
        
def main():
    for i in range(0):
        print(4, 5, 6, sep = "-")
        print(7, 8, end = "FDT\n")
    a = prefpy.aggregate.RankAggregator
    b = prefpy.aggregate.RankAggregator
    #x.get_alternatives()
    x = {}
    x[0] = 3
    print (x)
    
    voter1 = ["a", "b", "c"]
    voter2 = ["b", "a", "c"]
    voter3 = ["b", "c", "a"]
    voter4 = ["c", "a", "b"]
    voter5 = ["a", "c", "b"]
        
    votes = [voter1, voter2, voter3, voter4, voter5]
    alternatives = set(voter1)
    #for alt in alternatives:
    #    print (alt)
    #print (alternatives)
    print (borda(votes))
    print ([3,4] == [3,4])
    print (weightedMajorityGraph(votes))
    
main()
