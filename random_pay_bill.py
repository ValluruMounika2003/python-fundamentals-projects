import random

# names = input("Give me everybody's names, separated by a comma: ")
friends = ["mounika", "therija", "pavani", "raji", "maki", "mikasa",]

print(random.choice(friends))
random_index=random.randint(0,5)
print(friends[random_index])
