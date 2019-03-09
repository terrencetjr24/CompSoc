#test numbet 9

def print_none():
	print("no args")

def print_one(arg1):
	print ("argument 1", arg1)
	print (f"argument 1 {arg1}")

def print_two(arg1, arg2):
	print(arg1, arg2)

def print_idk(*args):
	print(args)
	#arg1, arg2, arg3 = args
	#print(arg1, arg2, arg3)

print_none()
print_one("My one argument\n")
print_two("Second argument ghee", "and the second of the second\n")
print_idk(3, 2, 1, 8)

print("vim is stupid")
