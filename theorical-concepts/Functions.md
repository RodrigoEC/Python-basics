# Functions in Python

Functions are blocks of code that perform a certain task previously 
established and can be reused in the future.

For example, look at the following code

```Python
wish_list = ["Car", "house", "better computer"]

print(len(wish_list))

output:
3
```
Here we're using python's built-in functions `print()` and `len()`, both of 
thosefunctions performs in a different way, the _len_ function for 
example returns the size of the wish_list and the _print_ function 
literally prints what the len() function returned.

## Creating functions 

We can create our own function using this structure:

```
def named_of_the_function():
    body
```

> :warning: warning: Be careful with the [`identation`](../README.md#identation).