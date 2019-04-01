{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

guests = ['kobe bryant', 'michael jordan', 'tom brady']

print(guests[0].title() + ", please join me for dinner.")
print(guests[1].title() + ", please join me for dinner.")
print(guests[2].title() + ", please join me for dinner.")

print("\nUnfortunately, " + guests[2].title() + " is unable to join us for dinner tonight.")

# Removing and replacing guest that can't make dinner
del(guests[2])
guests.insert(2, 'dwayne johnson')

print("Instead " + guests[2].title() + " will be joining Kobe, Michael, and myself to dinner.")

