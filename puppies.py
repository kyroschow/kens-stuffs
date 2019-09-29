numUsers = int(input("Number of users: "))

farAwayPuppies = []
for userIndex in range(numUsers):
    userPosition = input(f"Position of User {userIndex + 1} : ").split()
    numPuppies = int(input(f"Number of puppies for User {userIndex + 1}: "))
    for puppyIndex in range(numPuppies):
        puppyPosition = input(f"Position of Puppy {puppyIndex + 1}: ")
        if abs(int(puppyPosition[0]) - int(userPosition[0])) - abs(int(puppyPosition[1]) - int(userPosition[1])) > 10:
            farAwayPuppies.append(f"Puppy {puppyIndex + 1} (User {userIndex + 1})")

if len(farAwayPuppies) == 0:
    print("No puppies too far away")
else:
    print(" and ".join(farAwayPuppies), end=" ")
    print("too far away")
