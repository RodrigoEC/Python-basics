# Conditional statements

Let's say that you're on a trip and the road splits in two and you
have to decide which path you're gonna follow, the if statement works just
like that, you establish a conditional statement that shows our code how to behave if something happens.

Python has three basic types of conditional statements `if`, `elif` and `else`.

__Example:__ Creating a function "print_name" that works differently depending on the name that is passed as parameter.
```Python
def print_name(name):
    if name == "Rodrigo": # Establish a initial condition 
        print("Hi Rodrigo! That's my name too")
    elif name == "Leandra": # If previous conditions are not satisfied
        print("Hi Liendri! what are you doing here?") 
    else: # If no conditions are satisfied the code runs this line 
        print(f"Hi {name} how are you doing?") 
```
