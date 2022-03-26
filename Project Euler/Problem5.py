'''
Scenario:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
#Answer = 232792560
#------------------------------factorization code 
#Improved on from Problem 3
def prime_factorization(x):
    '''x is input to be factored, returns list of prime factors; 12 -> [2,2,3]'''
    
    def check_prime(x):
        '''x is input to be checked, returns divisors in tuple form (i1, i2) if not prime, boolean True otherwise'''
        #take value x and see if divisible by 2 through x/2 (cut in half since values past x/2 are unnecessary)
        #if x is divisible by any number not 1 or itself, then it's not prime
        for i in range(2, x//2):
            if x % i == 0:
                i1 = i
                i2 = int(x / i)
                return (i1, i2)
        return True
    
    primes = []
    not_primes = [x]
    templist = []
    
    #runs through list [not_primes], filters into lists [primes] and [templist] using check_prime()
    #avoids issue of: (don't mutate lists you're iterating on) by using fresh list each loop
    #converts [templist] into [not_primes] then empties [templist]
    while len(not_primes) != 0:
        for e in not_primes:
            if check_prime(e) == True:
                primes.append(e)
            else:
                L1 = check_prime(e)
                templist.append(L1[0])
                templist.append(L1[1])

        not_primes = templist
        templist = []

    return primes

'''
#testing values
B = prime_factorization(5933940200)
print(B)
'''

def list_to_dict(list1):
    '''takes input [list1], returns dictionary {dict1}; [2,2,3,5,5,5] -> {2:2,3:1,5:3}'''

    #use remove_duplicates to create a list of keys
    def remove_duplicates(L1):
        '''input: L1 list, returns modified_list with duplicates removed'''
        modified_list = []
        for e in L1:
            if e not in modified_list:
                modified_list.append(e)
        return modified_list
    
    #create baseline dictionary to fill in with values
    A = remove_duplicates(list1)
    dict1 = dict.fromkeys(A, 0)

    #increment value associated with key by one for every additional time it shows up
    for key in dict1:
        for e in list1:
            if key == e:
                dict1[key] += 1
        
    return dict1

'''
#testing values
C = list_to_dict(B)
print(C)
'''

def dictionary_cat(D1, D2):
    '''Combines two dictionaries, D1 and D2, returns D3; D3 = D1 union D2'''
    D3 = {}
    for key1 in D1:
        if D2.get(key1) == None:
            D3[key1] = D1[key1]
        elif D2.get(key1) != None:
            if D1[key1] >= D2[key1]:
                D3[key1] = D1[key1]
            else:
                D3[key1] = D2[key1]
    for key2 in D2:
        if D1.get(key2) == None:
            D3[key2] = D2[key2]
            
    return D3

'''
#testing values
X = {2:3, 3:4, 5:1, 7:2, 13:1}
Y = {2:1, 3:2, 5:2, 7:4, 11:2}
print(dictionary_cat(X, Y))
'''

def key_to_power(D1):
    '''input is dictionary D1, returns integer; {2:1,3:2} -> 18'''
    total = 1
    for key in D1:
        value = D1[key]
        total = total * (key ** value)
    return total


'''
#testing values
D = {2:3, 3:4, 5:1, 7:2}
print(key_to_power(D))
'''

#-------------------------Solution
'''Solvable using just lists, but wanted to use dictionaries to get practice using them.
Also using lists would probably be way more efficient'''
#get prime list for each value (prime_factorization)
#converts a list into a suitable dictionary (list_to_dict)
#combines dictionaries together (dictionary_concatenation)
#takes key and takes it to its value's power (key_to_power)
#solution: combines all functions together into a working solution (lowest_common_multiple)


def lowest_common_multiple(L1):
    '''
    input: integer inputs in a list 
    returns: lowest common multiple of those inputs as integer
    [1,2,3,4,5,6,7,8,9,10] = 2520
    '''
    templist1 = []
    for e in L1:
        e_factored = prime_factorization(e)
        templist1.append(e_factored)
    #makes lists of factored values and nests them in a container list: templist1
    
    templist2 = []
    for e in templist1:
        e_dict = list_to_dict(e)
        templist2.append(e_dict)
    #converts lists of factored values into dict and nests them in a new container list: templist2  
    
    while len(templist2) > 1:
        D1 = templist2.pop(0)
        D2 = templist2.pop(0)
        D3 = dictionary_cat(D1, D2)
        templist2.append(D3)
    #takes index 0 and 1 from nested list [templist2] and combines them into a new dict
    #then appends back into templist2, and repeats until templist2 has a single element
    
    tempdict = templist2[0]
    #pull out nested dict
    
    solution = key_to_power(tempdict)
    
    return solution
        



#take variable number of inputs from user and puts *args into dictionary (need to figure out)
#unpack dictionary into their variable names and values
#use prime_factorization to convert each variable into a list of its primes
#use list_to_dict to convert those lists into dicts
#dictionary_cat to combine all variables into one
#use key_to_power to output result


#testing values
Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Z1 = [11,12,13,14,15,16,17,18,19,20]
print(lowest_common_multiple(Z)) 
print(lowest_common_multiple(Z1))
