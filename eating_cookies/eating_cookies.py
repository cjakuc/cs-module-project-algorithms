from itertools import combinations_with_replacement, permutations, product
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # if n == 0:
    #     return 1

    # # https://www.geeksforgeeks.org/python-itertools-product/
    # solutions = []
    # for x in range(1,n+1):
    #     temp = product([1,2,3], repeat = x)
    #     for y in temp:
    #         if sum(y) == n:
    #             solutions.append(y)
    
    # return len(solutions)

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache is not None and cache[n] > 0:
        return cache[n]
    else:
        if cache is None:
            cache = [0 for i in range(n+1)]
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
