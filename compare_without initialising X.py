print("Number Comparator")

while True:
        
    a = float(input("\nEnter value of First Number :"))
    b = float(input("Enter value of Second Number :"))

    if a>b:
        print(a, "greater than", b)
    elif a<b:
        print(b, "greater than", a)
    elif a==b:
        print("Haha Both are equal.....!!!!!!!")

    x = input("\nEnter 1 to try again others to exit:")
    if(x != '1'):
        break

#Use Try Except statements for getting first and second number
