#Request input from user
print("Enter your annual salary:")
annual_salary = float(input())

print("Enter the percent of your salary to save,"
    " as a decimal:") 
portion_saved = float(input())

print("Enter the cost of your dream home:")
total_cost = float(input())

print("Enter the semi-annual raise, as a decimal")
semi_annual_raise = float(input())


#Initial constants
portion_down_payment = (total_cost * .25)
annual_percentage_return = float(.04)
r = annual_percentage_return



#variables needed for while loop
months = 0
monthly_returns = float(0)
current_savings = float(0)
#while loop to determine months needed
while portion_down_payment > current_savings:
    
    #how much you save from your salary each month
    salary_saved_per_month = ((annual_salary / 12) 
                            * (portion_saved))
    
    
    #how savings changes due to investing
    monthly_returns = (current_savings * r / 12)
    current_savings = (salary_saved_per_month
                       + current_savings
                       + monthly_returns)
    
    months = months + 1   
    
    #salary change due to raise
    if months % 6 == 0:
        annual_salary = (annual_salary
                         + annual_salary
                         * semi_annual_raise)
    else:
        continue
    

print("Number of months: " + str(months))

