#!/usr/bin/python3

import json 

# data serialization: python dict to json str

my_dict = {"key1" : 1, "key2" : 2, "key3": True}
my_json = json.dumps(my_dict)
print(my_json)

# can expand variables

test_id = 1
test_name = "test"
test_dict = {test_id : {"name": test_name}}
test_json = json.dumps(test_dict)
print(test_json)

# dumps() can take params to personalize the output (ex: skipkeys, sort_keys)

toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
sorted_json = json.dumps(toy_conditions, sort_keys=True, indent=" ⮑ ")
print(sorted_json)

# write json file (dump())

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking",],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading",],
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking",],
    },
  ],
}

with open("store.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dog_data, write_file, indent=" ⮑ ")
    
# data deserializatin: json str to python dict

# serialization </=> deserialization
dog_registry = {1: {"name": "Frieda"}}
dog_json = json.dumps(dog_registry, indent=True)
print(dog_json)

new_registry = json.loads(dog_json)
print(new_registry)