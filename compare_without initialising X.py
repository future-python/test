print("Number Comparator")

while True:
        
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))

    if a>b:
        print("a greater than b")
    elif a<b:
        print("b greater than a")
    elif a==b:
        print("a equals to b")

    x = int(input("Enter 1 to try again or 0 to exit:"))

    if(x != 1):
        break
