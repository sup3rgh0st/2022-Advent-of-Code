


print("Day 01 - Advent of Code")

highestCalories = 0 # Highest calorie count so far
currentCalories = 0 # Current calorie count

with open('01_data.txt', 'r') as f:
    for line in f:
        if line == '\n': # New Line denotes a New Elf
            if currentCalories > highestCalories:
                highestCalories = currentCalories
            currentCalories = 0
        else: # Continue Elf
            currentCalories += int(line)
    
    # Last elf isn't terminated with a new line. Either sanitize the data by adding one or have this final check.
    if currentCalories > highestCalories:
        highestCalories = currentCalories

print(highestCalories)
