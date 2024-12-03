def increase(nums):
    
    for i in range(len(nums) - 1):
        n1 = nums[i]
        n2 = nums[i+1]
        if n1 >= n2 or n2 - n1 > 3:
            return False
        
    return True


def decrease(nums):

    for i in range(len(nums) - 1):
        n1 = nums[i]
        n2 = nums[i+1]
        if n1 <= n2 or n1 - n2 > 3:
            return False
        
    return True



def main():
    with open("/Users/doc/Desktop/python projects/adevent of code/2024/day2/d2.txt", "r") as data:
        
        safeReports = 0

        for line in data:
            
            nums = line.strip().split(" ")
            nums = list(map(int, nums))

            print(nums)
            n1 = nums[0]
            n2 = nums[1]
            if n1 < n2:
                safe = increase(nums)
                if safe:
                    safeReports += 1

            if n1 > n2:
                safe = decrease(nums)
                if safe:
                    safeReports += 1


            print(safeReports)


if __name__ == "__main__":
    main()
