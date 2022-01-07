import json

values = []

path = r'C:\Users\Kompiuteris\Desktop\12sepNumbers.txt'
with open(path, 'r') as f:
    for line in f:
        line = line.strip()
        values.append(line)

integerValues = [int(numericString) for numericString in values]

orange = [1, 2, 3, 4, 5, 6, 7]
black = [8, 9, 10, 11, 12, 13, 14]
green = 0

for i in range (len(integerValues)):
    if integerValues[i] in orange:
        integerValues[i] = 'o'
    elif integerValues[i] in black:
        integerValues[i] = 'b'
    else:
        integerValues[i] = 'g'

current_streak = 0
max_streak = 0
streaksArray = []
streaksSum = 0

for j in range(len(integerValues)):
    if integerValues[j] == 'b' or integerValues[j] == 'g':
        current_streak += 1
    else:
        if current_streak > max_streak:
            streaksArray.append(current_streak)
            streaksSum += current_streak
            max_streak = current_streak
            current_streak = 0
            
        elif current_streak < max_streak:
            streaksArray.append(current_streak)
            streaksSum += current_streak
        current_streak = 0

print("Average streak " + str(streaksSum/len(streaksArray)))
print(streaksArray)
print(max_streak)