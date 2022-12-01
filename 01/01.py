


print("Day 01 - Advent of Code")

NUM_ELVES = 3 # Number of elves we want to track calories for
LOWEST_INDEX = NUM_ELVES-1 # Index of highestCalories that has the elf with the least amount of calories

highestCalories = [] # Highest calorie counts so far, index 0 being the highest
currentCalories = 0 # Current calorie count

# Helper that stores off a calorie value while popping off the lowest.
def insertCalorie(value):
    for x in range(len(highestCalories)):
        if value > highestCalories[x]:
            highestCalories.insert(x, value)
            break
    highestCalories.pop(-1) # End of array will always be the lowest


# Setup array with empty data, we allow for any number of elves
for x in range(NUM_ELVES):
    highestCalories.append(0)
    
with open('01_data.txt', 'r') as f:
    for line in f:
        if line == '\n': # New Line denotes a New Elf
            if currentCalories > highestCalories[LOWEST_INDEX]:
                insertCalorie(currentCalories)
            currentCalories = 0
        else: # Continue Elf
            currentCalories += int(line)
    
    # Last elf isn't terminated with a new line. Either sanitize the data by adding one or have this final check.
    if currentCalories > highestCalories[LOWEST_INDEX]:
        insertCalorie(currentCalories)

print(sum(highestCalories))
