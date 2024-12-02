import csv

leftCol, rightCol = [], []

# Getting the Data
with open(r"C:\Users\danie\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Advent of Code 2024\Advent-of-Code-2024\Day 1\AoC2024D1.csv") as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        leftCol.append(int(line[0]))
        rightCol.append(int(line[1]))
        # print(leftCol, rightCol)
        
# Gathering the similarty scores
similarityScore = 0
similarity = []
for entryL in leftCol:
    for entryR in rightCol:
        if entryL == entryR:
            similarityScore += 1
            # print(similarityScore, entryL)
    similarity.append(similarityScore * entryL)
    similarityScore = 0

# print(similarity)

# Getting the sum
sum = 0
for entry in similarity:
    sum += (int(entry))
print()
print(sum)