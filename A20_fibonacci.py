n=int(input("Enter how many fibonacci you want\n"))

l=[0,1]


for i in range(2,n):
    l.insert(i,l[i-1]+l[i-2])

print(l)





