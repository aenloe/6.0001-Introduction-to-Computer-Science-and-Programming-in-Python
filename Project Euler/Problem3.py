'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#-------------------attempted code that didn't work
'''
def prime_factors(x):
    list_of_primes = []
    L1 = [x]
    while L1 != []:
        for e in L1:
            for i in range(2, e):
                if e % i == 0:
                    x = e // i
                    L1.remove(e)
                    L1.append(x)
                    L1.append(i)
                    break
                print(list_of_primes)
                print(L1)
            list_of_primes.append(e)
    return list_of_primes

print(prime_factors(13195))
'''


'''
x = 13195
for a in range(2, x, -1):
    print(a)
    if x % a == 0:
        for b in range(2, a, -1):
            print(b)
            if a % b == 0:
                break
        print(a)       

#print(largest_prime_factor(13195))
'''

'''
        def largest_prime_factor(x):
    for a in range(((x//2)+1) , 1, -1):
        if x % a == 0:
            for b in range(((a//2)+1), 0, -1):
                if b == 1:
                    return a
                elif a % b == 0:
                    break
                

print("This is " + str(largest_prime_factor(60085147)))

def check_if_prime(x):
    for e in range(x-1, 1, -1):
        if x % e == 0:
            return False
    return True
'''
    
#-----------------Solution
#shitty solution see Problem 5 for more optimized version

def prime_factorization(x):
    '''
    uses function is_prime(x) while dividing values then sending those values to list primes
    '''
    
    def is_prime(x):
        '''
        returns boolean: True if prime, False otherwise. Meant for small values
        '''
        for e in range(2, x, 1):
            if x % e == 0:
                return False
        return True
    
    primes = []
    not_primes = [x]
    
    while not_primes != []:
        y = not_primes[0]
        if is_prime(y) == True:
            primes.append(y)
            not_primes.pop(0)
        else:
            for e in range(2, y+1, 1):
                if y % e == 0:
                    if is_prime(e) == True:
                        primes.append(e)
                        not_primes.pop(0)
                        not_primes.append(int(y/e))
                        break
                    else:
                        pass

    primes.sort()
    return primes[-1]

print(prime_factorization(600851475143))


