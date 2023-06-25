# Python If-else statements
Decision making is an essential aspect of programming, and Python provides several statements for implementing decision-making logic. In Python, decision making is primarily performed using if, if-else, and elif statements. This readme provides an overview of these statements along with code examples.

## Indentation in Python
Python uses indentation to define blocks of code. Statements at the same indentation level are part of the same block. It is customary to use four spaces for indentation in Python.

## If Statement
The if statement is used to test a specific condition. If the condition is true, a block of code (if-block) following the if statement will be executed.

### Syntax
    if condition:
    # block of statements

num = int(input("Enter the number: "))
if num % 2 == 0:
    print("The given number is even")


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("From the above three numbers, 'a' is the largest")
if b > a and b > c:
    print("From the above three numbers, 'b' is the largest")
if c > a and c > b:
    print("From the above three numbers, 'c' is the largest")


## If-else Statement
The if-else statement is used when there are two possible outcomes based on the condition. If the condition provided in the if statement is true, the code block following the if statement is executed. Otherwise, the code block following the else statement is executed.

### Syntax:

if condition:
    # block of statements
else:
    # block of statements (else-block)


