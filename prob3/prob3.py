def two_sum(nums, target):
    num_to_index = {}  # Create a dictionary to store numbers and their indices
    
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement needed
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], i]  # Return the indices of the two numbers
        
        # If the complement is not found, store the current number and its index
        num_to_index[num] = i
    
    return None  # If no solution is found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output will be [0, 1] because nums[0] + nums[1] equals 9.

