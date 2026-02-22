#Psitive no. from a range

def main():
    ch = "y"
    while ch=="y":
        l = list(map(int, input("Enter comma separated values: ").split(",")))
        print(list(filter(lambda x: x>0, l)))
        ch = input("Try again? (y/n): ").lower()
    print("Bye")

if __name__=="__main__":
    main()