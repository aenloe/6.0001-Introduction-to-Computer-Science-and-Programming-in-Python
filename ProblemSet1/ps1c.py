'''
Program purpose: Calculate the best savings rate as
a function of starting salary. 
Starts by creating a function that calculates savings
after 36 months. Uses that function to generate a list 
of savings based on savings rate. Uses bisection search
to find a savings that matches the down payment, and outputs
the index. Uses index to find savings rate.
'''

#Request input from user
starting_salary = int(input("Enter your annual salary: "))

#Initial constants
total_cost = float(1000000)
portion_down_payment = (total_cost * .25)
annual_percentage_return = float(.04)
semi_annual_raise = float(.07)
r = annual_percentage_return


def savings_after_36_months(portion_saved):
    
    '''function for current_savings after 36 months'''
    
    #initial variables needed for function
    months = 0
    monthly_returns = float(0)
    current_savings = float(0)
    global starting_salary
    annual_salary = starting_salary
    
    while months < 36:
        #how much you save from your salary each month
        salary_saved_per_month = ((annual_salary / 12) 
                                * (portion_saved))
        
        #how savings change due to investing
        monthly_returns = (current_savings * r / 12)
        current_savings = (salary_saved_per_month
                           + current_savings
                           + monthly_returns)
        
        #increment month to calculate new salary 
        #before entering new loop
        months = months + 1  
          
        #salary change due to raise
        if months % 6 == 0:
            annual_salary = (annual_salary
                             + annual_salary
                             * semi_annual_raise)
        
        
    
    return current_savings
    

#create initial list to eventually fill with data
list_savings = []
for i in range(0,10000):
    x = (i / 10000)
    list_savings.append(savings_after_36_months(x))


def bisection_search(x, list_y):
    
    '''
    Modified bisection search function
    attempts to match x to within 100 of list_y
    outputs ANY match, may have multiple matches
    '''
    
    #initial variables
    iterations = 1
    lower_bound = 0
    upper_bound = len(list_y) - 1
    
    while iterations <= len(list_y):
        
        #calculate y_index to be midpoint
        y_index = ((upper_bound + lower_bound) // 2)
        
        #check if x is within range of y
        if abs(x - list_y[y_index]) < 100:
            
            print("Best savings rate: " + str(y_index/10000))
            print("Steps in bisection search: " + str(iterations))
            return
            
        #check what y_index equals, then compare y to x
        if list_y[y_index] < x:
            lower_bound = y_index + 1
        elif list_y[y_index] > x:
            upper_bound = abs(y_index - 1)
        
        #update iterations
        iterations = iterations + 1
        
        #optional optimization code
        if y_index == upper_bound:
            break
        elif y_index == lower_bound:
            break
    
    print("It is not possible to pay the down payment in three years.")


bisection_search(portion_down_payment, list_savings)
