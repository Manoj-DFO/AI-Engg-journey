nums = [10, 5, 2, 7, 1, 9]
k = 15

def longest_sum(nums):

    prefix_sum = 0
    maximum = 0
    prefix_index = {0: -1}

    for i in range(len(nums)):

        prefix_sum += nums[i]

        target = prefix_sum - k

        if target in prefix_index:

            length = i - prefix_index[target]
            maximum = max(maximum, length)

        if prefix_sum not in prefix_index:

            prefix_index[prefix_sum] = i

    return maximum

print(longest_sum(nums))


#560. Subarray Sum Equals K