def maxProduct(arr):
    max_product = None

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # Nested loop to get distinct pairs
            product = arr[i] * arr[j]

            if max_product is None or product > max_product:
                max_product = product

    return max_product

print(maxProduct([2, 3, 4, 5, 6]))  # Should return 30 (6 * 5)
print(maxProduct([1, 2, 3, 4]))     # Should return 12 (4 * 3)
print(maxProduct([1, 1, 2, 2]))     # Should return None (There are no distinct integers)
print(maxProduct([-5, -3, -1, 0, 2])) # Should return 15 (-5 * -3)
print(maxProduct([5, 5, 8, 8, 7]))
print(maxProduct([5, 5, 5, 5, 7]))
print(maxProduct([5, 0, 8, -2, 7]))
print(maxProduct([5, -3, 8, -2, 7]))
