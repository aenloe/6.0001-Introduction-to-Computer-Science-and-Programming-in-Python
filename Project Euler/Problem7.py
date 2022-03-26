#---------------------naive solution

def xth_prime(x):
    '''input: int x represents the xth prime number, returns prime value'''
    L1 = []
    counter = 2
    while len(L1) < x+1: 
        for i in range(2, counter+1):
            if i == counter:
                L1.append(counter)
            elif counter % i == 0:
                break

        counter += 1
    return L1[x]

print(xth_prime(1001))

#-----------------------
#Sieve of Eratosthenes
