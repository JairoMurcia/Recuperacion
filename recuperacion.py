from functools import reduce
"""
1
"""
l=[[11,2,3],[4,5,6],[37,8,9],[10,11,12,13],[24,15,16]]

m=list(map(lambda x:[x[0]]+[x[len(x)-1]],l))

print("primer ejercicio ",m)

"""
2
"""
k=[12,15,34,20,80,92,24]

k=list(map(lambda x:list(str(x)),k))




perfecto=list(filter(lambda x :reduce(lambda a,b :int(a)%2==0 and int(b)%2==0,x),k))

perfecto=list(map(lambda a:reduce(lambda c,b:c+b,a),perfecto))
perfecto=list(map(lambda a:int(a),perfecto))
print("Segundo ejercicio ",perfecto)





"""
3
"""
s=list(map(lambda y :reduce(lambda a,b:a if a>b else b,y),l))
print("tercer ejercicio ",s)

"""
4
"""
ejemplo=[[80,82,46],[22,34,45],[2,43,29]]
t=lambda x:list(str(x))
ejemplo=list(map(lambda a :list(map(t,a))  ,ejemplo))
ejemplo=list(map(lambda a :list(filter(lambda h:reduce(lambda j,n:int(j)%2==0 and int(n)%2==0,h),a))  ,ejemplo))
ejemplo=list(filter(lambda a:a!=[],ejemplo))
ejemplo=list(map(lambda a:list(map(lambda h :reduce(lambda j,n:j+n,h),a)) ,ejemplo))
ejemplo=list(map(lambda a:list(map(lambda v:int(v),a)),ejemplo))
ejemplo=list(map(lambda y:reduce (lambda a,b:a if a<b else b,y) ,ejemplo))
print(ejemplo)




"""
5
"""

y=[3,244,16,25,40]

y=list(filter(lambda x: x<y[0]**5  ,y))
print("quinto ejercicio ",y)

"""
6
"""
z=[(6,3),(15,5),(5,1)]

lista=map(lambda x:x[0] if x[0] == (x[1]*(x[1]+1)/2) else 0,z)
suma=reduce(lambda a,b:a+b,lista)

print("sexto ejercicio",suma)
