print("Palindrome version 3")

string = input("enter word to check whether its a palindrom:")

length = int(len(string))
i = 0
j = length -1
for x in range(length):
	if(string[i] == string[j]):
		i+=1
		j-=1
		k = 1
	else:
		k = 0
		break

if(k == 1):
	print("Entered string is palindrome")
elif(k == 0):
	print("Entered string is not palindrome")





	


