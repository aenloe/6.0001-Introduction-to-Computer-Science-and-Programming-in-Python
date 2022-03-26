'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiple_L1(x):
    L1 = []
    total = 0
    for e in range(x):
        if e % 3 == 0:
            L1.append(e)
        elif e % 5 == 0:
            L1.append(e)
    
    for e in L1:
        total = total + e
    
    print (total)

multiple_L1(1000)
