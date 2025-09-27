d={
    "Apple": "A fruit that is typically red, green, or yellow.",
    "Banana": "A long, curved fruit that is yellow when ripe.",
    "Grapes": "Small, round fruits that grow in clusters on vines.",
    "Mango": "A tropical fruit with a sweet and juicy flesh.",
}

print(d['Apple'])


# Ading a new entry to the dictionary
d['Orange']="A round citrus fruit that is typically orange in color."

print(d)


# Updating an existing entry in the dictionary
d['Apple']="A sweet fruit that comes in various colors including red, green, and yellow."

print(d)

# Deleting an entry from the dictionary
del d['Banana']
print(d)



print("-------------------------------------------------------")

# Looping through the dictionary
for key in d.keys():
    value = d[key]
    print(key)
    print(value)



# Checking if a key exists in the dictionary
if 'Orange' in d:
    print(d['Orange'])


# Getting the number of entries in the dictionary
print(len(d))


# looping through key in the dictionary
for key in d:
    value = d[key]
    print(key)
    print(value)