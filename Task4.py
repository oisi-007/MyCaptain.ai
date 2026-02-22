#set operations

def main():
    a= set(map(int, input("Enter space-separted values for first set A: ").split(" ")))
    b= set(map(int, input("Enter space-separted values for second set B: ").split(" ")))
    print("A:",a,"\nB:",b)
    print("Union of A and B is",a|b)
    print("Intersection of A and B is", a&b)
    print("Difference of A and B is",a-b)
    print("Symmetric difference of A and B is", a^b)



if __name__=="__main__":
    main()