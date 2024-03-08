import sympy
a=[]
b=0
c=0
for i in sympy.primerange(1,4000):
    a.append(i)
    if sum(a)>=1000000:
        break
for i in range(len(a)):
    for d in range(i,len(a)):
        if sympy.isprime(sum(a[i:d])):
            if (d-i)>b:
                b=(d-i)
                c=sum(a[i:d])
print(c)

