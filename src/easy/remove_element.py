def remove_element(nums: list[int], val: int) -> int:
    """
    Adapt the partition function used in Quicksort.
    """
    length = len(nums)

    if length == 0:
        return 0

    if nums[-1] != val:
        try:
            r = nums.index(val)
        except ValueError:
            return length

        nums[-1], nums[r] = nums[r], nums[-1]

    k, i = 0, -1

    for j in range(length - 1):
        if nums[j] != val:
            i += 1
            k += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[-1] = nums[-1], nums[i + 1]

    return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3

    print(remove_element(nums=nums, val=val))
    print(nums)
