def summaryRanges(nums):
    result = []
    start = end = nums[0] if nums else None

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            end = nums[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + '->' + str(end))
            start = end = nums[i]

    if start is not None:
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + '->' + str(end))

    return result


nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))
