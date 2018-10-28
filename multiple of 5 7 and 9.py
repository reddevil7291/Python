n = eval(input("\nEnter any number:"))
t = (5,7,9)
if(not isinstance(n,int)):
    print("\nWrong Input")
else:
    if(n%t[0]==0 or n%t[1]==0 or n%t[2]==0):
        print("\nThe given number is a multiple ")
    else:
        print("\nThe given number is not a multiple")
