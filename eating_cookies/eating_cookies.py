from itertools import combinations_with_replacement, permutations, product
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n == 0:
        return 1

    # https://stackoverflow.com/questions/20193555/finding-combinations-to-the-provided-sum-value

    # vals = [1, 2, 3]
    # combinations = [comb for i in range(1, 20) for comb in combinations_with_replacement(vals, i) if sum(comb) == n]
    # return len(combinations)

    # https://stackoverflow.com/questions/13715786/list-all-the-permutation-to-sum-up-some-numbers-to-a-dest-number
    # findSubsets(list,sol,n):
    # choices = [1,2,3]
    # if (list.empty() and n == 0): #found a feasible subset!
    #     print sol 
    #     return
    # else if (n < 0): #bounding non feasible solutions
    #     return 
    # else if (list.empty()): #a solution that sums to a smaller number then n
    #     return
    # e = choices.pop(0)
    # sol = sol.add(e)
    # eating_cookies(list,sol,n-e)
    # sol <- sol.removeLast()
    # findSubsets(list,sol,n)
    # list.addFirst(e) #cleanup, return the list to original state

    # solutions = []
    # vals = [1, 2, 3]
    # combs = [comb for i in range(1, 20) for comb in combinations_with_replacement(vals, i) if sum(comb) == n]
    
    # for x in combs:
    #     temp = list(x)
    #     solutions.append(permutations(temp, inc))

    # return len(solutions)


    # https://www.geeksforgeeks.org/python-itertools-product/
    solutions = []
    for x in range(1,n+1):
        temp = product([1,2,3], repeat = x)
        for y in temp:
            if sum(y) == n:
                solutions.append(y)
    
    return len(solutions)

def eating_cookies2(n, lst):
    solutions = []
    for x in range(1,n+1):
        temp = product(lst, repeat = x)
        for y in temp:
            if sum(y) == n:
                solutions.append(y)
    
    return len(solutions)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
