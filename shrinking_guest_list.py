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

# Bigger table so adding more guests
print("\nGuess what we just got a bigger table!" + "\n")
guests.insert(0, 'kevin hart')
guests.insert(2, 'derek jeter')
guests.append('james bond')

print(guests[0].title() + ", we got a bigger table so please join us for dinner.")
print(guests[1].title() + ", more guests will be joining us for dinner tonight.")
print(guests[2].title() + ", we got a bigger table so please join us for dinner.")
print(guests[3].title() + ", more guests will be joining us for dinner tonight.")
print(guests[4].title() + ", more guests will be joining us for dinner tonight.")
print(guests[5].title() + ", we got a bigger table so please join us for dinner.")

# Bigger dinner table will not be ready in time for dinner. Only two guests can join dinner tonight.
print("\nI'm sorry guests but the bigger dinner table will not be ready in time for dinner.")

name = guests.pop()
print("Sorry, James Bond dinner was cancelled.")

name = guests.pop()
print("Sorry, Dwayne Johnson dinner was cancelled.")

name = guests.pop()
print("Sorry, MJ dinner was cancelled.")

name = guests.pop()
print("Sorry, Derek Jeter dinner was cancelled.")

print(guests)

# Guests still invited
print("\n" + guests[0].title() + ", you are still invited to dinner with Kobe and I.")
print(guests[1].title() + ", you are still invited to dinner with Kevin and I.")

# Use del to empty out list
del(guests[0])
del(guests[0])

print(guests)
