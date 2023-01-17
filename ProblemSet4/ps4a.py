# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    def insertion(char: str, string: str) -> list:

        output = []
        end = len(string) + 1

        for index in range(0, end):
            x = (string[0:index] + char + string[index:end])
            output.append(x)

        return output

    def recursion(sequence: str) -> list:
        #base case
        if len(sequence) == 1:
            return sequence

        #recursive step
        result = []
        sliced_end_char = sequence[-1]
        recursive_returned_list = recursion(sequence[0:-1])

        for element in recursive_returned_list:
            result.extend(insertion(sliced_end_char, element))

        return result

    return recursion(sequence)

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected output:' , '[some list of values]')
    print('Actual Output:', get_permutations(example_input))
    

