string1= input("Enter first string\n")
string2=input("Enter second string\n")
string3=''

for i in range(len(string1)):
    if(string1[i].isupper()):
        string3 +=string1[i]

for i in range(len(string2)):
    if (string2[i].isupper()):
        string3 += string2[i]

print(string3)