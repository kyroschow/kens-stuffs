riverLength = int(input('Length of riverfront: '))
numAnimals = int(input('Number of animals: '))
animals = []
for i in range(numAnimals):
    position = input('Animal ' + str(i + 1) + ': ').split()
    animals.append(position)

lastOccupiedIndex = -1
maxWhiteSpaceLength = 0
i = 0

while i < riverLength:
    for animal in animals:
        if int(animal[0]) <= i <= int(animal[1]):
            maxWhiteSpaceLength = max(maxWhiteSpaceLength, i - lastOccupiedIndex - 1)
            lastOccupiedIndex = int(animal[1])
            i = lastOccupiedIndex
            break
    i += 1
maxWhiteSpaceLength = max(maxWhiteSpaceLength, riverLength - lastOccupiedIndex - 1)

print(maxWhiteSpaceLength)
