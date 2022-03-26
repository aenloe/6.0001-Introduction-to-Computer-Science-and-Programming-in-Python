'''
1000 digit Fibonacci number
'''

def fibonacci():
    L1 = [1,1]
    while len(str(L1[-1])) < 1000:
        x = L1[-1] + L1[-2]
        L1.append(x)
        
    return len(L1)

print(fibonacci())