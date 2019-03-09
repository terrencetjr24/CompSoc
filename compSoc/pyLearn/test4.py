#Imma beast
string = "whats up kids"
f_string = f"look how i can automatically say, {string}"

print(string)
print(f_string)

empty_f_string = "Is this a valid string? {}"
a = "nah fam"
b = "just playing"
print(empty_f_string.format(a))
print(empty_f_string.format(b))
print(empty_f_string.format(True))

first_half = "I just wanna "
second_half = "paaaartaaay. Go Go Go"

print(first_half + second_half)

divider = "-p"
dividing_line = "{}"

print(dividing_line.format(divider * 10))