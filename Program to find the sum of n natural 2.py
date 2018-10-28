print("Program to Find the sum of n Natural Numbers")

n = eval(input("\nEnter the value of n:"))
sum = float

if(not isinstance(n,int)):
    print("\nWRONG INPUT")

else:
        if(n<=0):
            print("\nERROR")
        else:
            sum1 = (n*(n+1))/2
            print("The sum is ",sum1)
