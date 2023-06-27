# Python Scope
In Python, scope refers to the visibility and accessibility of variables, functions, and objects within a program. Understanding how scope works is crucial for writing clean and maintainable code. Python has four types of scopes:

## Local Scope: 
Variables defined within a function or method have a local scope. They are accessible only within the function or method where they are defined. Once the function or method completes execution, the local variables are destroyed.

## Global Scope: 
Variables defined outside of any function or method have a global scope. They can be accessed from anywhere within the program. Global variables remain in memory throughout the lifetime of the program.

## Enclosing Scope: 
In Python, we can define functions within other functions, creating a nested structure. The inner function has access to variables in its enclosing function's scope. This is known as an enclosing scope.

Built-in Scope: Python provides a set of built-in functions and objects that are accessible from anywhere within the program. These functions and objects are part of the built-in scope. Examples include print(), len(), str(), etc.


