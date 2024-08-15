# Simple function displaying recursion, given a list of numbers

def add(nums):
    total = 0
    for num in nums:
        total += num
    return total

def sum(nums):
    # stopping condition
    if not nums:
        return 0
    print("Calling sum(%s)" % nums[1:])
    remaining_sum = sum(nums[1:])
    print("Call to sum(%s) returning %d + %d" %(nums, nums[0], remaining_sum))
    return nums[0] + remaining_sum

print(sum([1, 2, 7, 9]))