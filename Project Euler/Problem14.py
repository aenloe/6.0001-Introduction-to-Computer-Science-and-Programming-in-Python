'''
Longest Collatz Sequence
Which starting number under 1 million produces the longest chain?
Answer: 837799, took roughly ~50 sec to compute
'''

#---------------------------------
#make a function defining the chain process, outputting the result into a list to later measure
#have a main function that iterates through values up to a million 
#main function maintains only one list at any one time, the longest list
#---------------------------------

def collatz_sequence(x):
    L1 = [x]
    
    while x != 1:
        if x % 2 == 0:
            x = int(x / 2)
            L1.append(x)
        elif x % 2 == 1:
            x = (3 * x) + 1
            L1.append(x)        
    
    return L1



def solution():
    L1 = collatz_sequence(1)
    for x in range(2,1000000):
        if len(collatz_sequence(x)) > len(L1):
            L1 = collatz_sequence(x)
    return L1

print(solution())