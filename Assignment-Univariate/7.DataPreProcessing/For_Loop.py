
numbers = [1, 2, 3, 4, 5]

# ----- Example 1: Traditional 'for' loop -----
# 1. Initialize an empty list to store the squared numbers.
squared_numbers_loop = []

# 2. Loop through each number in the 'numbers' list.
for number in numbers:
    # 3. Square the current number.
    square = number ** 2
    
    # 4. Add the squared number to our new list.
    squared_numbers_loop.append(square)

# Print the result
print(f"Result from traditional loop: {squared_numbers_loop}")

# ----- Example 2: List Comprehension -----

# A list comprehension combines the initialization, loop, and append
# into a single, concise line. The syntax is [expression for item in iterable].
squared_numbers_comprehension = [number ** 2 for number in numbers]

# Print the result
print(f"Result from list comprehension: {squared_numbers_comprehension}")