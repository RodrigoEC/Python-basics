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
def name_of_the_function(parameters):
    body
```
where:
__def:__ Key word to start the creation of the function;
__parameters:__ Are all the things that the function needs to receive to 
be able to work properly, like the list in the function `len()` i.g;
__body:__ Is all the block of code that makes the function work, it can have
the statement `return`, which means that the functon returns something, or not.

> :warning: warning: Be careful with the [`identation`](../README.md#identation).


__Example 01:__ Creating a function that returns the number of characters in a word
```Python
def count_characters(word):
    if type(word) == 'str':
        return len(word)

count_characters('caveiras')

output:
8
```

__Example 02:__ Creating a function that doesn't returns anything, just
prints something

```Python
def we_are_all_calarrara(name):
    print(f"{name} calarrara the rattlesnake from Piauí")

we_are_all_calarrara("jorgina")

output:
Jorgina Calarrara the rattlesnake from Piauí
```