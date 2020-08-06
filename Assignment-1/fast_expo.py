def mul(a,b):
    r=len(a)
    c=len(b[0])
    res=[[0 for i in range(c)] for j in range(r)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j]+=a[i][k]*b[k][j]
    return res

def fast_exp(m,n):
    num=bin(n).replace("0b","")
    num=num[::-1]
    term=m
    if(num[0]=='1'):
        res=m
    else:
        res=[[0 for i in range(len(m[0]))] for j in range(len(m))]
        for i in range(len(m)):
            res[i][i]=1

    for i in range(1,len(num)):
        term=mul(term,term)
        if(num[i]=='1'):
            res=mul(res,term)
    return res

m=[[3,1],[4,2]]
n=int(input("Enter n: "))
res=fast_exp(m,n)
for i in res:
    print('\n')
    for j in i:
        print(j,end='\t')

'''
------SAMPLE OUTPUT------
Enter n: 4


269     105 

420     164

------------------------
'''