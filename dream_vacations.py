{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

locations = ['bora bora', 'macau', 'sicily', 'rome', 'tokyo']

print("Here is the original list:")
print(locations)

print("\nHere is the sorted list:")
print(sorted(locations))

print("\nList is still in its original form:")
print(locations)

print("\nHere is the list in reverse alphabetical order:")
print(sorted(locations, reverse=True))

print("\nList is still in its original form:")
print(locations)

print("\nHere is my list in reverse:")
locations.reverse()
print(locations)

print("\nReversing the order back to its original form:")
locations.reverse()
print(locations)

print("\nHere is my list in sort form:")
locations.sort()
print(locations)

print("\nHere is my list in reverse sort:")
locations.sort(reverse=True)
print(locations)

