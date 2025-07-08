# Working on a binary search

# [1,2,3,4,5,6,7]

# log of n to base 2

class Solution:
    def search(arr, target):
            
        low = 0
        high = len(arr) - 1 #6

        while low <= high:
            mid = (low + high) // 2 #3
            guess = arr[mid]

            if guess == target:
                return mid
            elif guess > target:
                high = mid - 1
            else:
                low = mid +1 
        return None

arr = [1, 2, 3, 4, 5, 6, 7]

# print(Solution.search(arr, 1))  # 🟢 Expect: 0
# print(Solution.search(arr, 4))  # 🟢 Expect: 3
# print(Solution.search(arr, 7))  # 🟢 Expect: 6
# print(Solution.search(arr, 8))  # 🔴 Expect: None (not in list)
# print(Solution.search(arr, 0))  # 🔴 Expect: None (not in list)
# print(Solution.search([], 1))   # 🔴 Expect: None (empty list)


"""

EXERCISES
1.1 Suppose you have a sorted list of 128 names, and you’re searching
through it using binary search. What’s the maximum number of
steps it would take?
1.2 Suppose you double the size of the list. What’s the maximum
number of steps now?


"""






       
            

        
        