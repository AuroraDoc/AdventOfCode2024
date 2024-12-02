with open("d1puzzle.txt", "r") as data:

    left = []
    right = []

    total = 0

    for line in data:
        nums = line.strip().split("   ")

        left.append(int(nums[0]))
        right.append(int(nums[1]))

    for num in left:
        curr = right.count(num)

        total += (num * curr)

    print(total)
