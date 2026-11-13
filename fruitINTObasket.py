
def total_fruits(fruits):
    left = 0
    max_fruits = 0
    fruit_count = {}

    for right in range(len(fruits)):
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        # Keep at most two fruit types
        while len(fruit_count) > 2:
            left_fruit = fruits[left]
            fruit_count[left_fruit] -= 1

            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]

            left += 1

        # Update maximum window length
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


fruits = [1, 2, 1, 2, 3]
print("Maximum fruits:", total_fruits(fruits))
