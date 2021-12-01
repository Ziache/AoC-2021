with open("./input", "r") as f:

    # read the lines and convert them into integers
    depths = [int(l) for l in f.readlines()]

# init state
depth = depths[0]
count = 0

for d in depths[1:]:
    if d > depth:
        count += 1
    else:
        pass
    depth = d

print(count)
