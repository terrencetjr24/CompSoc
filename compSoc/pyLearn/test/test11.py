#test11

list = ["apple", "banana", "cucumber", "dairy", "enchaladas"]

print(f"range of 5 = {range(5)}")

print(f"Length of the original list is {len(list)}")


for i in range(len(list)):
	print(f"Index {i}, item: {list[i]}")

#or if we don't care about the index we can

for item in list:
	print(f"Item: {item}")

for i, item in enumerate(list):
	print(f"index {i}, Item: {item}")
