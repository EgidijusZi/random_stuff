import json

values = []

path = r'C:\Users\Kompiuteris\Desktop\14sepNumbers.txt'
with open(path, 'r') as f:
    for line in f:
        line = line.strip()
        values.append(line)

integerValues = [int(numericString) for numericString in values]

orange = [1, 2, 3, 4, 5, 6, 7]
black = [8, 9, 10, 11, 12, 13, 14]
green = 0

for i in range (2973):
    if integerValues[i] in orange:
        integerValues[i] = 'o'
    elif integerValues[i] in black:
        integerValues[i] = 'b'
    else:
        integerValues[i] = 'g'

print(integerValues)

i = 0 #start of pattern
j = 4 #for merging/splicing
k = 4 #next element after pattern of 4 values

#valuesForPattern = [', '.join(integerValues[i:j])]
#print(valuesForPattern)

permutationsOfColours = {
'o, o, o, o' : [0, 0, 0, 0],
'o, o, o, b' : [0, 0, 0, 0],
'o, o, o, g' : [0, 0, 0, 0],
'o, o, b, o' : [0, 0, 0, 0],
'o, o, b, b' : [0, 0, 0, 0],
'o, o, b, g' : [0, 0, 0, 0],
'o, o, g, o' : [0, 0, 0, 0],
'o, o, g, b' : [0, 0, 0, 0],
'o, o, g, g' : [0, 0, 0, 0],
'o, b, o, o' : [0, 0, 0, 0],
'o, b, o, b' : [0, 0, 0, 0],
'o, b, o, g' : [0, 0, 0, 0],
'o, b, b, o' : [0, 0, 0, 0],
'o, b, b, b' : [0, 0, 0, 0],
'o, b, b, g' : [0, 0, 0, 0],
'o, b, g, o' : [0, 0, 0, 0],
'o, b, g, b' : [0, 0, 0, 0],
'o, b, g, g' : [0, 0, 0, 0],
'o, g, o, o' : [0, 0, 0, 0],
'o, g, o, b' : [0, 0, 0, 0],
'o, g, o, g' : [0, 0, 0, 0],
'o, g, b, o' : [0, 0, 0, 0],
'o, g, b, b' : [0, 0, 0, 0],
'o, g, b, g' : [0, 0, 0, 0],
'o, g, g, o' : [0, 0, 0, 0],
'o, g, g, b' : [0, 0, 0, 0],
'o, g, g, g' : [0, 0, 0, 0],
'b, o, o, o' : [0, 0, 0, 0],
'b, o, o, b' : [0, 0, 0, 0],
'b, o, o, g' : [0, 0, 0, 0],
'b, o, b, o' : [0, 0, 0, 0],
'b, o, b, b' : [0, 0, 0, 0],
'b, o, b, g' : [0, 0, 0, 0],
'b, o, g, o' : [0, 0, 0, 0],
'b, o, g, b' : [0, 0, 0, 0],
'b, o, g, g' : [0, 0, 0, 0],
'b, b, o, o' : [0, 0, 0, 0],
'b, b, o, b' : [0, 0, 0, 0],
'b, b, o, g' : [0, 0, 0, 0],
'b, b, b, o' : [0, 0, 0, 0],
'b, b, b, b' : [0, 0, 0, 0],
'b, b, b, g' : [0, 0, 0, 0],
'b, b, g, o' : [0, 0, 0, 0],
'b, b, g, b' : [0, 0, 0, 0],
'b, b, g, g' : [0, 0, 0, 0],
'b, g, o, o' : [0, 0, 0, 0],
'b, g, o, b' : [0, 0, 0, 0],
'b, g, o, g' : [0, 0, 0, 0],
'b, g, b, o' : [0, 0, 0, 0],
'b, g, b, b' : [0, 0, 0, 0],
'b, g, b, g' : [0, 0, 0, 0],
'b, g, g, o' : [0, 0, 0, 0],
'b, g, g, b' : [0, 0, 0, 0],
'b, g, g, g' : [0, 0, 0, 0],
'g, o, o, o' : [0, 0, 0, 0],
'g, o, o, b' : [0, 0, 0, 0],
'g, o, o, g' : [0, 0, 0, 0],
'g, o, b, o' : [0, 0, 0, 0],
'g, o, b, b' : [0, 0, 0, 0],
'g, o, b, g' : [0, 0, 0, 0],
'g, o, g, o' : [0, 0, 0, 0],
'g, o, g, b' : [0, 0, 0, 0],
'g, o, g, g' : [0, 0, 0, 0],
'g, b, o, o' : [0, 0, 0, 0],
'g, b, o, b' : [0, 0, 0, 0],
'g, b, o, g' : [0, 0, 0, 0],
'g, b, b, o' : [0, 0, 0, 0],
'g, b, b, b' : [0, 0, 0, 0],
'g, b, b, g' : [0, 0, 0, 0],
'g, b, g, o' : [0, 0, 0, 0],
'g, b, g, b' : [0, 0, 0, 0],
'g, b, g, g' : [0, 0, 0, 0],
'g, g, o, o' : [0, 0, 0, 0],
'g, g, o, b' : [0, 0, 0, 0],
'g, g, o, g' : [0, 0, 0, 0],
'g, g, b, o' : [0, 0, 0, 0],
'g, g, b, b' : [0, 0, 0, 0],
'g, g, b, g' : [0, 0, 0, 0],
'g, g, g, o' : [0, 0, 0, 0],
'g, g, g, b' : [0, 0, 0, 0],
'g, g, g, g' : [0, 0, 0, 0]
}

numberOfGreens = 0

while k < 2973:
    mergedValuesForPattern = [', '.join(integerValues[i: j])]
    valueAfterMerge = integerValues[k]
    mergedValuesForPatternToString = str(mergedValuesForPattern)[1:-1] #removing square brackets
    simplifiedMergedValuesForPatternToString = mergedValuesForPatternToString[1:-1] #removing quotes
    if simplifiedMergedValuesForPatternToString in permutationsOfColours:
        if valueAfterMerge == "o":
            permutationsOfColours[simplifiedMergedValuesForPatternToString][0] += 1
        elif valueAfterMerge == "g":
            permutationsOfColours[simplifiedMergedValuesForPatternToString][1] += 1
            numberOfGreens += 1
        elif valueAfterMerge == "b":
            permutationsOfColours[simplifiedMergedValuesForPatternToString][2] += 1
        else:
            permutationsOfColours[simplifiedMergedValuesForPatternToString][3] += 1
    i += 1
    j += 1
    k += 1

#print(permutationsOfColours)

jsonObject = json.dumps(permutationsOfColours, indent = 4)
print(jsonObject)
print(numberOfGreens)