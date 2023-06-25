# Python Loops
Loops in Python are used to execute a block of code repeatedly until a certain condition is met. Python provides two types of loops: for loop and while loop. This readme provides an overview of both types of loops along with code examples.

## For Loop
The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects. It allows executing a block of code a fixed number of times, once for each item in the sequence.

Syntax:

python
Copy code
for item in sequence:
# block of statements

### Example 1: Iterating over a list

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
print(fruit)
	Example 2: Using the range function

	python
	Copy code
	for i in range(1, 5):
		print(i)
		While Loop
		The while loop is used to repeatedly execute a block of code as long as a certain condition is true. It allows executing the block of code an unknown number of times until the condition becomes false.

###		Syntax:

		while condition:
# block of statements
		Example 1: Printing numbers from 1 to 5

		i = 1
		while i <= 5:
print(i)
	i += 1
	Example 2: Taking user input until a certain condition is met

	name = ''
	while name != 'quit':
	name = input("Enter a name (or 'quit' to exit): ")
	print("Hello, " + name + "!")
	Loop Control Statements
	Python provides control statements that allow modifying the behavior of loops.

	break statement: It is used to exit the loop prematurely.
	continue statement: It is used to skip the current iteration and move to the next iteration.
	Example: Using loop control statements

	for i in range(1, 10):
		if i == 5:
		break  # exit the loop when i is equal to 5
		if i % 2 == 0:
	continue  # skip even numbers
	 print(i)
	 Nested Loops
	 Python allows nesting loops, which means you can have a loop inside another loop. This is useful when dealing with complex scenarios that require iterating over multiple sequences.

	 Example: Nested loops

	 for i in range(1, 4):
		 for j in range(1, 4):
			 print(i, j)
			 In this example, the outer loop iterates from 1 to 3, and for each iteration, the inner loop iterates from 1 to 3 as well, resulting in all possible combinations of i and j being printed.

			 Feel free to explore and modify these code examples to understand the behavior and usage of loops in Python. Loops are powerful constructs that enable efficient and repetitive processing of data and tasks.

