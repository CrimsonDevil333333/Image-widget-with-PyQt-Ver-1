import os

path = 'images\\'

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
