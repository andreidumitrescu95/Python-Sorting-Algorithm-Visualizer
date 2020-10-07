from Display.display import update_display

def merge_sort(height):
    """
    height of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(height) < 2:
        return height

    mid = len(height) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_height = merge_sort(height[:mid])
    right_height = merge_sort(height[mid:])

    return merge(left_height, right_height)

def merge(left, right):
    """
    Traverse both sorted sub-heightays (left and right), and populate the height heightay
    """
    height = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            height.append(left[i])
            i += 1
        else:
            height.append(right[j])
            j += 1
    height += left[i:]
    height += right[j:]

    #update_display(50)

    return height