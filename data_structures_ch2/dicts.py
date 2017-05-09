# messing around with dicts
dictt = {'Jonathan': 27, 'Marisa': 28}  # creating a dict
dictt['bill'] = 29  # add to dict
dictt['jonathan']  # search for value by key
del dictt['bill']  # remove item from dict
print(dictt)  # access contents of dict
len(dictt)  # determining size of dict
for k, v in dictt.items():  # traversing the dict
    print(k, v)
