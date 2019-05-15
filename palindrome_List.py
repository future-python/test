print("Palindrome Check")
stg = input("Enter input string to check Palindrome :")
length = len(stg)

for x in range (length-1):
    if stg[x] == stg[length-1-x]:
        print("Letter ",x," Matches")
        s = "Palindrome"
    else:
        s = "not a palindrome"
        break
print("Your String",stg,"is",s)
