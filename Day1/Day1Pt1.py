with open("d1puzzle.txt", "r") as data:
    
    left = []
    right = []

    total = 0

    for line in data:
        nums = line.strip().split("   ")

        left.append(nums[0])
        right.append(nums[1])

    left.sort()
    right.sort()
    
    for i in range(len(left)):
        curr = int(left[i]) - int(right[i])
        curr = abs(curr)
        total += curr

    print(total)

