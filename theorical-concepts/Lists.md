# Lists in python

In python we have the concept of __lists__, which are data structures 
that can store any sorts of items. By the way, list in python are not 
restrictive by type, thus we can have a list with strings and integers i.g.

> :warning: Even if it is possible to add different data types in a list
it's usually a bad habit to do that.

__Example:__ List of game names
```python
games = ["Don't starve", "Terraria", "The last of us", "Battle Block Theater"]
```
> The example above is going to be used in the following example as a base to the operation.

## Lists handling

In python there's a ton of things that we can do with lists, here I'm gonna
be covering a feel of them.

---
### Slice

Using slice we can create a "sublist" of a bigger list using the following
structure:

```Python

list_name[startIndex, endIndex]

```
where:
- list_name: Name of the list that is gonna be sliced, always in **snake_case**.
- startIndex: List index where the slice is going to start.
- endIndex: The list index where the slice is going to stop.


__Example:__ Using the games example that was set before, we're going to select only 
the first two games of the list **games**

```Python
games[0:2]

Output:
["Don't starve", "Terraria"]
```

> As we can see the second index (THe las of us) was not shown in the
output, that is because the endIndex in the slice operation is not considered.

---
### Append Method

This method allows us to add a new item to the end of a list using the 
following structure:

```python
named_list.append(item)
```

__Example:__ Add "Enter the gungeon" to the games list

```
games.append(Enter the gungeon)
print(games)

output:

["Don't starve", "Terraria", "The last of us", "Battle Block Theater", "Enter the gungeon"]
```
---
### Remove Method

This method allows us to remove a item of a list by it's value

Structure:

```Python
named_list.remove(item)
```

__Example:__ Remove "the last of us" from the games list
```Python
games.remove("The las of us")

output:
["Don't starve", "Terraria", "Battle Block Theater"]
```


---
### Max()

Receives a list of values and returns the highest value. 

> When comparing strings this method uses the letter's order in the alphabet
as metric to compare string. For example, "a" is lower than "z".

```Python

max(named_list)

outputs:
"The last of us"
```

---
### Min()
Receives a list of values and returns the lowest value. 

> When comparing strings this method uses the letter's order in the alphabet
as metric to compare string. For example, "a" is lower than "z".

```Python

min(named_list)

outputs:
"Battle block theater"
```

---
### Sorted()
Receives a list of values and returns a ordered list. 

> When comparing strings this method uses the letter's order in the alphabet
as metric to compare string.

```Python

sorted(named_list)

outputs:
["Battle block theater", "Don't starve", "Terraria", "The last of us"]
```
# Tuples

Python tuples are like lists, but can't be manipulated, which means that
the method append nor the method remove here. In python tuples are created
following this structure:

```Python
tuple_name = (item1, item2, item3)
```