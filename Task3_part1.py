#Fibonacci Series program:

def fibonacci(n):
    a=0
    b=1
    while n>0:
        print(a, end=" ")
        a,b=b,a+b
        n-=1
    print("\n")

if __name__=="__main__":
    ch="y"
    while (ch=="y"):
        n = int(input("Enter no. of terms for Fibonacci Series: "))
        fibonacci(n)
        ch= input("Try again? (y/n): ").lower()
    print("Bye")