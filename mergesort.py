from typing import List
import matplotlib.pyplot as plt

def plot_list(arr: List[int], step: str) -> None:
    """
    Plotting the current state of the list.
    """
    plt.clf()  # Clear the current figure
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(f'{step} - List state')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.pause(0.5)  # Pause to create an animation effect

def merge_sort(arr: List[int], plot_steps: bool = True, depth: int = 0) -> None:
    """
    Sorts arr in-place using the merge sort algorithm and optionally plots each step.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        merge_sort(left, plot_steps, depth + 1)
        merge_sort(right, plot_steps, depth + 1)

        left_index, right_index, merge_index = 0, 0, 0

        # Merging sorted halves
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                arr[merge_index] = left[left_index]
                left_index += 1
            else:
                arr[merge_index] = right[right_index]
                right_index += 1
            merge_index += 1

        # Copying the remaining elements of left, if any
        while left_index < len(left):
            arr[merge_index] = left[left_index]
            left_index += 1
            merge_index += 1

        # Copying the remaining elements of right, if any
        while right_index < len(right):
            arr[merge_index] = right[right_index]
            right_index += 1
            merge_index += 1

        # Plotting current state after merging
        if plot_steps:
            step_description = f'Merge step at depth {depth}'
            plot_list(arr, step_description)

## List for Sorting
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Initial plot
plt.ion()  # Enable interactive mode
plt.figure(figsize=(10, 6))
plot_list(my_list, 'Initial List')

# Sort the list with dynamic plotting
merge_sort(my_list)

# Final plot to show sorted list
plt.ioff()  # Disable interactive mode
plt.show()  # Display the final sorted state
