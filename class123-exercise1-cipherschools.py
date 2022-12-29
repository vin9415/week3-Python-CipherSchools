n=int(input("Enter a number: "))
keys=[]
for a in range(1,n+1):
    keys.append(a)
values=list(map(lambda x:x**3,keys))
data=dict(zip(keys,values))
print(data)