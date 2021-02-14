import numpy as np
def coinFlip(p):    
    #perform the binomial distribution (returns 0 or 1)    
    result = np.random.binomial(1,p)#return flip to be added to numpy array    
    return result
'''Main Area'''
#probability of heads vs. tails. This can be changed.
probability = .5
#num of flips required. This can be changed.
n = 10#initiate array
fullResults = np.arange(n)#perform desired numbered of flips at required probability set above
for i in range(0, n):    
    fullResults[i] = coinFlip(probability)    
    i+=1#print results
print("probability is set to ", probability)
print("Tails = 0, Heads = 1: ", fullResults)
#Total up heads and tails for easy user experience 
print("Head Count: ", np.count_nonzero(fullResults == 1))
print("Tail Count: ", np.count_nonzero(fullResults == 0))