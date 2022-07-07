def get_permutations(sequence):
    '''
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    '''
    
    #Base case:
    if len(sequence) == 1:
        return sequence
    
    #Recursive case:
    else:
        #pull first string (e) from string (sequence) 
        #nextrecursion is list of strings 
        #then return a list with (e) in every position in (sequence)
        newlist = []
        e = sequence[0]
        nextrecursion = get_permutations(sequence[1:])
        for x in nextrecursion:
            
        
        #needs to return a list of strings
        return nextrecursion 
    
x = 'a'
y = 'bcd'        
def testfoo(char, string):
    '''Function that does the following: given 'a', and 'bcd'
    give output ['abcd', 'bacd', 'bcad', 'bcda'] '''
    #initial case
    counter = 1
    o_list = []
    initial = char + string[1:]
    o_list.append(initial)
    
    combo = string[0:counter] + char + string[counter:]
    #subsequent cases
    while counter < (len(string) + 1):
        o_list.append(combo)
        counter += 1
    
    return o_list

print(testfoo(x,y))

