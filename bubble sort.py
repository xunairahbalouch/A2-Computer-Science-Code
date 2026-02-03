def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        swapped = False
        # Last i elements are already in place, so we ignore them
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                # Swap elements
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return my_list