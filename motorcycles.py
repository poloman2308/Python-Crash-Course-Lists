{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[-1] = 'honda'
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

motorcycles.append('harley')
print(motorcycles)

# Adding elements to a list
bikes = []
bikes.append('honda')
bikes.append('yamaha')
bikes.append('suzuki')
bikes.append('ducati')
bikes.append('harley')
bikes.append('bmw')
print(bikes)

# Insert items in a list
bikes.insert(0, 'mophead')
print(bikes)

#remove elements
del bikes[0]
print(bikes)
del bikes[-1]
print(bikes)

#pop items
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

print(motorcycles)
motorcycles.insert(2, 'ducati')
motorcycles.insert(3, 'suzuki')
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.insert(3, 'ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

