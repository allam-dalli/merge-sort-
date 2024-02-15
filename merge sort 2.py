def merge_sort(arr):
    print(f"\n\n   Splitting: {arr}")
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves using divide-and-conquer
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    print(f"\n\n   Merged: {arr}")


if __name__ == "__main__":
    # Example usage
    input_numbers = input('Numbers (separated with space): ')
    input_array = [int(num) for num in input_numbers.split()]

    print("\n\n    Original Array:", input_array)
    merge_sort(input_array)
    print("\n\n   Sorted Array:", input_array)
