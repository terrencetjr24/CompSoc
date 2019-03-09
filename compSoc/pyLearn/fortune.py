#fortune teller

import random

def getAnswer(num):
	if num == 1:
		return "Most def"
	elif ((num > 1) & (num <= 5)):
		return "Prolly Not"
	elif num > 5:
		return "Dont do it"

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)