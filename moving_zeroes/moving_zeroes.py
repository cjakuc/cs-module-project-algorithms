'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    temp = []
    zeros = []
    for x in arr:
        if x != 0:
            temp.append(x)
        else:
            zeros.append(x)
    for x in zeros:
        temp.append(x)

    return temp


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")