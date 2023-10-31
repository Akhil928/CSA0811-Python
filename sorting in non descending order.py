def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    start = left

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    end = right

    return [start, end] if start <= end else [-1, -1]
