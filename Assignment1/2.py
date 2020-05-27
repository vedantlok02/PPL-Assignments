import random
min = 1
max = 6
roll_again = "Y"
while(roll_again == "Y"):
	roll_again = input("Do you want to roll again ? [Y/n]?")
	if(roll_again == "Y"):
		print(random.randint(min, max))
	elif(roll_again == "n"):
		break
	else :
		print("Please enter a valid input !!")

