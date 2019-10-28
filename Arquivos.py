import os
cwd = os.getcwd()

print(os.listdir(cwd))
print (cwd)

print (os.path.abspath("te"))
font = open("teste.json", "w")


print(font.write("harry potter, what are you doing there man?\n"))

# the write function only works with str types, so if we want to add other values, we're gonna
# need to convert them.

print(font.write(str(511)))
font.close()