#list
animals = ["monkey", "lion", "rabbit", "tiger"]

#empty list
empty = []

#manipulating list

#accessing to data
print(animals[2])
print(animals[-1])


#adding data
animals.append("flog")
print(animals)


#assigning data
animals[1] = "Korea lion"
print(animals)

#deleting data
del animals[0]
print(animals)

#list slicing
print(animals[1:3])
print(animals[:]) #all
print(animals[:3])
print(animals[1:])

#list length
print(len(animals))

#list sort
animals.sort()
print(animals)

animals.sort(reverse=True)
print(animals)