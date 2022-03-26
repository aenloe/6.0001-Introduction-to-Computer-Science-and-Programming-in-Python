'''
Pentagonal numbers: 
Pn = n(3n-1)/2

P(n) = list of every pentagonal number
D = |Pj - Pk|
Find smallest D such that Pj-k and Pj+k are both elements in P(n)
'''

def pentagonal_number(n):
    p_n = (n*(3*n - 1))/2
    return int(p_n)

#generate P(n)
P_n = [pentagonal_number(n) for n in range(100)]
print(P_n)