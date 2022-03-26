'''
Sudoku problem solver
'''

#-------------------------------------Overall Plan
'''
Need to figure out multiple algorithms before arriving at final solution:
1) Need to create a data structure to import any sudoku into and base my solving algorithms around that structure
2) Need to devise a working algorithm (naive, improved, optimal) to provide a finalized output
3) Need to devise a checking function to evaluate whether the solution works
    -can use checking function during the working algorithm to verify
    -needs to be able to 


'''
#-------------------------------------Data Structure Approach
'''
Dictionary data structure.
Have keys represent three coordinate points. (x,y,z) representing (column, row, square)
    -(2,5,s4); column 2, row 5, square 4 (read top to bottom, left to right, 9 squares) 
Have values represent the possible values that can exist at that coordinate:
    -[1,2,3,4,5,6,7,8,9]; every value possible i.e. unsolved
    -[1,2,3]; eliminated choices
    -[3]; solved, the answer is 3 in that spot
'''



#-------------------------------------Solving Algorithm Ideas

#Naive Deduction
'''
Systematically go through all keys and eliminate any known values from their pool of possible values 
(c1,c2,x) - check all surrounding tile values
(x,c1,c2) - check all row values
(c1,x,c2) - check all column values
'''


#-------------------------------------Input Conversion code

'''
#Incomplete code to open file to draw input from
with open('p096_sudoku.txt', 'r') as f:
    lines = f.readlines()
print(lines)

'''

#Functions to help parse input from given file into something the program can manipulate
def parse_string(string): 
    '''
    converts a string to a list of characters
    input = '123' -> output = ['1','2','3']
    '''
    return [char for char in string]

def convert_int(input_list):
    '''
    creates a new list and converts all values into integer types
    '''
    list_copy = []
    for element in input_list:
        list_copy.append(int(element))
    return list_copy

def convert_values(input_list):
    '''
    iterates through a list, converts all 0 values into a list from 1 to 9
    input input = [0, 1] -> output = [[[1,2,3,4,5,6,7,8,9], 1]
    '''
    list_to_return = []
    for element in input_list:
        if element == 0:
            list_to_return.append([1,2,3,4,5,6,7,8,9])
        else:
            list_to_return.append([element])
        
    return list_to_return



#testvalues to use until input conversion code gets completed
pre_int = parse_string('003020600900305001001806400008102900700000008006708200002609500800203009005010300')
post_int = convert_int(pre_int)
parsed_values_for_algorithm = convert_values(post_int)



#-------------------------------------Key Template

key_list_template = [
                    (1,1,1), (1,2,1), (1,3,1), (1,4,2), (1,5,2), (1,6,2), (1,7,3), (1,8,3), (1,9,3),
                    (2,1,1), (2,2,1), (2,3,1), (2,4,2), (2,5,2), (2,6,2), (2,7,3), (2,8,3), (2,9,3),
                    (3,1,1), (3,2,1), (3,3,1), (3,4,2), (3,5,2), (3,6,2), (3,7,3), (3,8,3), (3,9,3),
                    (4,1,4), (4,2,4), (4,3,4), (4,4,5), (4,5,5), (4,6,5), (4,7,6), (4,8,6), (4,9,6),
                    (5,1,4), (5,2,4), (5,3,4), (5,4,5), (5,5,5), (5,6,5), (5,7,6), (5,8,6), (5,9,6),
                    (6,1,4), (6,2,4), (6,3,4), (6,4,5), (6,5,5), (6,6,5), (6,7,6), (6,8,6), (6,9,6),
                    (7,1,7), (7,2,7), (7,3,7), (7,4,8), (7,5,8), (7,6,8), (7,7,9), (7,8,9), (7,9,9),
                    (8,1,7), (8,2,7), (8,3,7), (8,4,8), (8,5,8), (8,6,8), (8,7,9), (8,8,9), (8,9,9),
                    (9,1,7), (9,2,7), (9,3,7), (9,4,8), (9,5,8), (9,6,8), (9,7,9), (9,8,9), (9,9,9)
                     ]

#-------------------------------------Code

'''This will be the starting point for any algorithm routine to solve'''
algorithm_input = dict(zip(key_list_template, parsed_values_for_algorithm))
print(algorithm_input)



def naive_deduction_algorithm(sudoku_data):
    '''Given a dictionary form of the sudoku data to input, mutate input dictionary
    Maybe have an option to create a visible table output'''
    
    def check_row(x):
        '''Input: Tuple-key from dictionary data'''
        if len(algorithm_input[x]) == 1:
            return
        column = x[1]
        tile = x[2]
        for e in range(1,10):
            if len(algorithm_input[e,column,tile]) == 1:
                value_to_remove = algorithm_input.get((e,column,tile))
                list_to_modify = algorithm_input.get(x)
                try:
                    list_to_modify.remove(value_to_remove[0])
                except:
                    pass
    
    def check_column(x):
        '''TBD'''
        if len(algorithm_input[x]) == 1:
            return
        row = x[0]
        tile = x[2]
        for e in range(1,10):
            if len(algorithm_input[row,e,tile]) == 1:
                value_to_remove = algorithm_input.get(row,e,tile)
                list_to_modify = algorithm_input.get(x)
                try:
                    list_to_modify.remove(value_to_remove[0])
                except:
                    pass
        
    def check_tile(x):
        '''TBD'''
        if len(algorithm_input[x]) == 1:
            return
        row = x[0]
        column = x[1]
        for e in range(1,10):
            if len(algorithm_input[row,column,e]) == 1:
                value_to_remove = algorithm_input.get(row,column,e)
                list_to_modify = algorithm_input.get(x)
                try:
                    list_to_modify.remove(value_to_remove[0])
                except:
                    pass

    list_of_sudoku_keys = algorithm_input.keys()
    def per_dot(x):
        check_row(x)
        check_column(x)
        check_tile(x)
        
    for x in list_of_sudoku_keys:
        per_dot(x)
    
    
naive_deduction_algorithm(algorithm_input)
print(algorithm_input)