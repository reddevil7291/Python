n = eval(input("\nEnter any number:"))

if(not isinstance(n,int)):
    print("\nWrong Input")
else:
    if(n%7):
        print("\nThe given number is a multiple ")
    else:
        print("\nThe given number is not a multiple")
