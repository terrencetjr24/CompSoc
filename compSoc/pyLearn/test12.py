
a = 3
b = 5

if(a==3):
	print("a == 3")
elif(b == 5):
	print("b == 5")
else:
	print("Nothing is true and the world is gonna end")


i = 0;
while (i != 10):
	i+=1

	if i==3:
		print(f"This is the third iteration ({i})")
		continue
	print(f"The iteration is: ({i})")

	if i ==7:
		print("i is equal to seven so breaking")
		break
