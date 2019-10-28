#   The dbm module only accepts str or bytes types, so the pickle module helps us "translate" amoust 
#any type of object into the string type.

import dbm
import pickle

db = dbm.open("pickle", "c")
a_list = [1, 2, 4]
a_list_translated = pickle.dumps(a_list)

db["list1"] = a_list_translated
print(a_list_translated)

a_list_translated_back = pickle.loads(a_list_translated)
print(a_list_translated_back)

#--------------------------------------------------------
explain = open("explain_Pickle", "w")

text = """The thing is:
      We can store lists into a data store with the pickle module, being by that way more easyer to 
    store thing that are not just strings or bytes, but any kind of data structure or object."""

explain.write(text)
explain.close()