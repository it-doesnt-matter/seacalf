# How to Customize the Datasets

## Table of Contents
- [Introduction](#introduction)
- [Changing the Keys](#changing-the-keys)
- [Removing Members](#removing-members)

## Introduction
This tutorial applies mostly to the datasets in JSON, YAML, CSV and XML format. In the following examples, we'll use the countries.json file and we'll explain everything using [JSON terminology](https://www.json.org/json-en.html).

All the example code is in Python, but for most other commonly used programming languages it should be similar. If you have any questions regarding this tutorial or other types of modifications, feel free to open a discussion.

## Changing the Keys
The Countries dataset is one big JSON object, where each member itself is an object, representing one country from ISO 3166-1. Those country objects use their Alpha-3 code as key. If for example you don't find that intuitive, you could change the keys. (As the Alpha-3 code is included in each country object, you don't have to worry about losing any data.) In the following code snippet, we'll change the dataset to use the English short name as key, instead of the Alpha-3 code.

```python
# we import the json module, which is part of the standard library
import json

# we open the desired file and load the data into a Python dictionary
with open("countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

# we use a dictionary comprehension to create a new dictionary and overwrite the old data
countries = {country["name"]["short"]: country for country in countries.values()}

# we open the file once again and write our new data to it
with open("countries.json", "w", encoding="utf-8") as file:
    json.dump(countries, file, ensure_ascii=False, indent=2)
```

In the example above, we used a dictionary comprehension to modify the data, but that is not the only way to do accomplish our goal. You could for example also use a for loop to iterate over each country instead.

Even though I refer to it as "changing" the keys, this is in the case of Python technically not correct. You can't change the key of a dictionary entry, instead you have to create a new entry with the updated key and delete the entry with the old key or alternatively create a whole new dictionary, like we did in the example above. If you are using another programming language/module, this might be different.

## Removing Members
In case that a dataset is too big and you want to reduce its size, you could delete some members that you don't need. If for example you don't need all the translations of the country names, you could do the following:

```python
# we import the json module, which is part of the standard library
import json

# we open the desired file and load the data into a Python dictionary
with open("countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

# we use a for loop to iterate over each country and delete its translations
for country in countries.values():
    del country["translations"]

# we open the file once again and write our new data to it
with open("countries.json", "w+", encoding="utf-8") as file:
    json.dump(countries, file, ensure_ascii=False, indent=2)
```

In case you want to keep only a very small subset of all the members, it might be easier to create a new dataset, instead of deleting the many unneeded members. In the following example, we'll create a new dataset, which contains only the English, short name and the capital.

```python
# we import the json module, which is part of the standard library
import json

# we open the desired file and load the data into a Python dictionary
with open("countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

# we initialize a dictionary to hold our new dataset
new_countries = {}

# we use a for loop to iterate over the original data and
# to copy the desired members to our new dictionary
for key, country in countries.items():
    new_countries[key] = {
        "name": country["name"]["short"],
        "capital": country["capital"]
    }

# we open the file once again and write our new data to it
with open("countries.json", "w+", encoding="utf-8") as file:
    json.dump(new_countries, file, ensure_ascii=False, indent=2)
```