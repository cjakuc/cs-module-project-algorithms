'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    for x in arr:
        temp = arr.count(x)
        if temp == 1:
            return x

def single_numner(arr):
    counts = {}
    for x in arr:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1
    for k, v in counts.items():
        if v == 1:
            return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")