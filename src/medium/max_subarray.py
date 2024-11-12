def maximum_subarray(nums: list[int]) -> int:
    total = 0
    max_sum = nums[0]

    for num in nums:
        total += num

        max_sum = max(total, max_sum)

        total = max(total, 0)

    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print(maximum_subarray(nums=nums))
