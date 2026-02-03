def recursive_binary_search(my_list, search_item, low, high):
    # Base Case 1: Search space exhausted
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # Base Case 2: Item found
    if my_list[mid] == search_item:
        return mid
    # Recursive Cases
    elif my_list[mid] < search_item:
        return recursive_binary_search(my_list, search_item, mid + 1, high)
    else:
        return recursive_binary_search(my_list, search_item, low, mid - 1)