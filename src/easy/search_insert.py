def search_insert(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while high >= low:
        mid = (low + high) // 2

        val = nums[mid]

        if target == val:
            return mid

        if target > val:
            low = mid + 1
        else:
            high = mid - 1

    return high + 1


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 7

    print(search_insert(nums, target))
