'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     # Your code here
#     final = []
#     for x in range(len(nums)-k+1):
#         temp = nums[x:(x+k)]
#         max_num = temp[0]
#         for y in temp:
#             if y > max_num:
#                 max_num = y
#         final.append(max_num)

#     return final

# def sliding_window_max(nums, k):
#     # Your code here
#     if len(nums) == k:
#         return max(nums)

#     else:
#         i = 0
#         final = []
#         while i < len(nums) - k + 1:
#             final.append(sliding_window_max(nums[i:i+k], k))
#             i += 1
#         return final

def sliding_window_max(nums, k):
    # Your code here
    i = 0
    final = []
    while i < len(nums) - k + 1:
        final.append(max(nums[i:i+k]))
        i += 1
    return final


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
