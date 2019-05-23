print("Number Comparator")

while True:
        
    a = float(input("Enter value of a :"))
    b = float(input("Enter value of b :"))

    if a>b:
        print(a, "greater than", b)
    elif a<b:
        print(b, "greater than", a)
    elif a==b:
        print(a, "equals to", b)

    x = input("Enter 1 to try again others to exit:")
    if(x != '1'):
        break
