#test 10

exampleList = []

exampleList.append("Hello")
exampleList.append(2)
exampleList.append(True)

print(exampleList[2])
print(exampleList[1])
print(exampleList[0])


print(f"Size of list before empty {len(exampleList)}")

exampleList.clear()
print(f"Size of list after emptying {len(exampleList)}")

exampleList = [4 ,10, 22, 35, 1, 9, 3, 15]
print(f"List before sorting {exampleList}")

exampleList.sort()
print(f"List after sorting {exampleList}")

exampleList.reverse()
print(f"List in reverse order {exampleList}")

exampleList.pop()
print(f"'Popped' last item from list {exampleList}")

exampleList.insert(1,999)
print(f"After adding 999 into the 1-index {exampleList}")

exampleList.insert(1,10)
exampleList.insert(1,10)
print(f"After adding 2 10s into the 1-index {exampleList}")
print(f"The number of 10s in the list {exampleList.count(10)}")

exampleList.remove(10)
print(f"After removing the first occuring 10 {exampleList}")

exampleList.remove(10)
print(f"After removing the next occuring 10 {exampleList}")

exampleList.remove(10)
print(f"After removing the first occuring 10 {exampleList}")