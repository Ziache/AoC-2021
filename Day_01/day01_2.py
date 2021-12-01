with open("./input", "r") as f:

    # read the lines and convert them into integers
    depths = [int(l) for l in f.readlines()]

# create the sums list
sums3 = [depths[i] + depths[i-1] + depths[i-2] for i in range(2, len(depths))]

# init state
sum3 = sums3[0]
count = 0

for s in sums3[1:]:
    if s > sum3:
        count += 1
    else:
        pass
    sum3 = s

print(count)
