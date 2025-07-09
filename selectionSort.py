class Solution:

    @staticmethod
    def find_smallest(arr):
        smallest = arr[0]              # Assume the first number is the smallest
        smallest_index = 0             # Store the index of the assumed smallest value

        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i     # Update index when a new smallest is found
        
        return smallest_index          # Return after checking the whole list

    @staticmethod
    def selection_sort(arr):
        new_arr = []
        copy = list(arr)               # Make a copy so we don't modify the original

        for i in range(len(copy)):
            smallest = Solution.find_smallest(copy)
            new_arr.append(copy.pop(smallest))
        return new_arr


"""
 the above program takes in an array and tries to sort it in an ascending order with two functions one finding the smallest value returning it
 and the second function picking it to create a new array with the values sorted.
 this takes (O(n2))
"""