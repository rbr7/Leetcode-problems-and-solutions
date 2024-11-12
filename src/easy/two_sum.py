def binary_search(
    indices: list[int],
    nums: list[int],
    key: int,
    low: int,
    high: int,
    a_idx: int,
) -> int:
    while high >= low:
        mid = (high + low) // 2
        mid_idx = indices[mid]

        if mid_idx != a_idx and nums[mid_idx] == key:
            return mid_idx

        if nums[mid_idx] >= key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def two_sum_sol1(nums: list[int], target: int) -> list[int]:
    indices = sorted(range(len(nums)), key=lambda x: nums[x])

    high = len(nums) - 1

    for idx in indices:
        a = nums[idx]
        b = target - a
        b_idx = binary_search(indices, nums, key=b, low=0, high=high, a_idx=idx)
        if b_idx != -1:
            return [idx, b_idx]


def two_sum_sol2(nums: list[int], target: int) -> list[int]:
    idx_map = {}

    for idx, num in enumerate(nums):
        b = target - num
        if b in idx_map:
            return [idx, idx_map[b]]
        idx_map[num] = idx


if __name__ == "__main__":
    nums = [0, 3, -3, 4, -1]
    target = -1
    result = two_sum_sol1(nums=nums, target=target)

    print(result)

    result = two_sum_sol2(nums=nums, target=target)

    print(result)
