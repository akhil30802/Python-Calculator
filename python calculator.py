#This is my first python program, it is a simple calculator.

def a():
	print("\n  ---Basic Calculator Program---")
	print("1) Addition")
	print("2) Subtraction")
	print("3) Multiplication")
	print("4) Division")
	print("5) Exit Calculator")

	option = float(input("Enter your operation: "))

	if option == 5:
		exit()

	operand1 = float(input("Please enter your first operand: "))
	operand2 = float(input("Please enter your second operand: "))

	if option == 1:
		print("result:     " , operand1 + operand2)
		a();

	if option == 2:
		print("result:     " , operand1 - operand2)
		a();

	if option == 3:
		print("result:     " , operand1 * operand2)
		a();

	if option == 4:
		print("result:     " , operand1 / operand2)
		a();

	return

a();