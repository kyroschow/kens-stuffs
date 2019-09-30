sentence = input("Text: ")

maxWordSize = 0
lastNotAlpha = -1
for i in range(len(sentence)):
    if not sentence[i].isalpha():
        maxWordSize = max(maxWordSize, i - lastNotAlpha - 1)
        lastNotAlpha = i

print(maxWordSize)
