str = input("Enter a string for a palindrome check\n")
flag=0;
for i in range(len(str)):
    if(str[i] == str[-(i+1)]):
        flag+=0;
    else:
        flag+=1;


if(flag!=0):
    print("String is not a palindrome")
else:
    print("string is a palindrome")