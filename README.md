# Python Basics

I truly believe that it's only possible to be really good at something complex if we fully understand the basics of the thing we're trying to be an expert in. 

Thus the goal of this repository is for me to register all of my progress "relearning" python from basic to advanced.

<div>
    <i>Wish me luck</i><br>
    <img src="./images/fingers-crossed.gif">
</div>

> Content that are too big I decided to leave just a link here to another
file so the README.md just contains some initial content and a bunch of links
to another files in this repository. Said that I hope you enjoy reading the following
cotent!

## Index
- [About Python](#about-python)
- [Lists](./theorical-concepts/Lists.md)
- [Dictionary](./theorical-concepts/Dictionary.md)



## About Python

### Snake Case
The standard variable name pattern in Python is called `Snake Case` and 
by that we say that variable must start with a lowercase letter and the
words are separated by a underscore ("_").

__Example:__ 
```Python
default_variable = "I'm a default variable"
```
---
### Identation

Instead using curly brackets ("{}") like java or the end statement like in matlab
Python uses `identation` to determine the end and beginning of a block of code.

In this next example we're going to see why identation is so important in python.

Case1:
```Python
is_true = False

if is_true == True:
    print("I found the truth!")

output: (there's no output)
```

Case2:
```Python
is_true = False

if is_true == True:
print("I founf the truth!")

output:
I found the truth!
```

As we can see in the second case the code printed "I found the truth",
something the shouldn't happen in view of the _is_true_ value is not True.

Well, what happened? Because of identation the print() function in the second
case didn't go through the "if" statement and wasn't filtered, something 
that didn't happened in the first, and correct, case.  

:warning: Be careful with identation in python!
---
### Dynamically typed language

Python is a `dynamically typed language` which means that we don't need to explicite the _type_ of the variables that we are creating. Because of that we can change the variable type just by changing it's value type, as we can see in the following example

__Ex:__ 
```Python
    my_name_is_julia = "Hy my name is julia"
    my_name_is_julia = 1423
```


