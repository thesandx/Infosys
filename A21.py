item=input("Enter name of furniture\n")

quan= int(input("Enter quantity of furniture\n"))

furniture=["Sofa set","Dining table","T.V Stand","Cupboard"]

cost=[20000,8500,4599,13920]

if(item in furniture and quan>0):
    index=furniture.index(item)
    bill=quan*cost[index]
    print("Total bill of",quan,item,"is",cost[index],"*",quan,"=",bill)

else:
    bill=0
    print("Error\nbill is",0)