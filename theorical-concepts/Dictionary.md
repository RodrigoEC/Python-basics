# Dictionaries

Dictionaries are python structures that allows us to associate key and value,
where key is like the "index" reference of the value in dictionaries.

Structure:
```Python
dict_name = {key1: value, key2: value, key3:value}
```

__Example:__ Dictionary that associates the name of a game with it's 
score at Steam. We're going to be using this example in the following 
topics.

```Python
dict_games = {
                "Don't starve" : 10,
                "Terraria" : 10,
                "The last of us" : 9.5,
                "Battle block theater" : 8.4
             }
```

## Access a dictionary item

In stead of choosing the item by it's index in the list, here we access
the items by it's key value in the dictionary

__Example:__

```python
dict_games["Don't starve"]

output:
10
```

### dictionary.keys()

This command returns a list with all the existing dictionary keys.

__Example:__

```Python
dict_games.keys()

output:

["Don't starve", "Terraria", "The last of us", "Battle block theater"]
```

### dictionary.values()

This command returns a list with all the existing dictionary values.

__Example:__

```Python
dict_games.values()

output:

[10, 10, 9.5, 8.4]
```