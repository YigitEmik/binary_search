list1 = [1, 3, 5, 7, 10, 12, 25, 46]
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if low > high:
        return -1
    midpoint = (low + high) // 2
    # If midpoint equals to target we return midpoint
    if l[midpoint] == target:
        return midpoint
    # If target less than the midpoint we return all the variables as same as the beggining except high,
    # We are changing our high point to midpoint-1
    # For example [1, 3, 5, 10, 12, 15, 25] if we are looking for 3,
    # Our new high will be 5 and the rest values are same.
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)

    else:
        # target > l[midpoint]
        # Same logic as the high point but now we are increasing our low to change our low point
        return binary_search(l, target, midpoint+1, high)

print(binary_search(list1, 12))
