import csv
import numpy as np

values = []

path = r'C:\Users\Kompiuteris\Desktop\crashValues.csv'
with open(path, 'rU') as x:
    for line in x:
        cells = line.split(",")
        values.append((cells[0].strip().split(".")[0]))

print(values)

max_gap = 0
current_gap = 0

for value in values:
    if int(value) < 2:
        current_gap += 1
    else:
        if current_gap > max_gap:
            max_gap = current_gap

        current_gap = 0
else:
    if current_gap > max_gap:
        max_gap = current_gap

print(max_gap)

x = np.array(values)
y = x.astype(np.float)

unique_values = list(sorted(set(values)))
print(unique_values)
max_gap = 0
current_gap = 0

for unique_value in unique_values:
    for value in values:
        if value < unique_value:
            current_gap += 1
        else:
            if current_gap > max_gap:
                max_gap = current_gap

            current_gap = 0
    else:
        if current_gap > max_gap:
            max_gap = current_gap

    print('Value: {0}, Max gap: {1}'.format(unique_value, max_gap))
    