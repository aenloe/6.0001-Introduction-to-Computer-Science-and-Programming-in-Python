'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def is_palindrome(x):
    '''
    returns boolean: True if palindrome.
    implementation: converts to string, reads first half, reverses, compares with second half
    '''
    string_palindrome = str(x) #string
    length_palindrome = len(string_palindrome) #int
    first_half = [e for e in string_palindrome[0:length_palindrome//2]]

    if length_palindrome % 2 != 0:
        second_half = [e for e in string_palindrome[length_palindrome//2 + 1:]]
    else:
        second_half = [e for e in string_palindrome[length_palindrome//2:]]
    
    first_half_reversed = first_half[::-1]
    return first_half_reversed == second_half


def largest_palindrome(a, b):
    palindrome_list = []
    for a1 in range(a):
        for b1 in range(b):
            if is_palindrome(a1 * b1) == True:
                palindrome_list.append(a1 * b1)
            else:
                continue
    palindrome_list.sort()
    return(palindrome_list[-1])


print(largest_palindrome(999, 999))
