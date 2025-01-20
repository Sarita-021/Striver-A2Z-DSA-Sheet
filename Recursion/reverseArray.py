def reverse_array_extra_array(arr):
    rev_arr = arr[::-1]

    # Print reversed array
    print("Reversed Array:", end=" ")
    for i in rev_arr:
        print(i, end=" ")

# Example usage:
org_arr = [1, 2, 3, 4, 5]
reverse_array_extra_array(org_arr)
