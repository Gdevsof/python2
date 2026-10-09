name = "F3rry"

try: 
	user_input = input("Enter the name: ")
	if name == user_input:
		print(f"The {name} is the same as {user_input}")
	else:
		print(f"The input is invalid")
except ValueError:
		print(f"Invalid Input")