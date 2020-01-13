def merge_sort(items):
    if len(items) <= 1:
        return items
    
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    # return middle_index, left_split, right_split
    return merge(left_sorted,right_sorted)

# My Original Version
# def merge(left,right):
#     result = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#         else:
#             if len(left) > 0:
#                 result.append(left.pop(0))
#             if len(right) > 0:
#                 result.append(right.pop(0))
#     return result

# Version mostly matching CA Lesson
def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left

    if right:
        result += right

    return result


list = [2,3,4,5,6,1,4,6]

lst_1 = [2,3,4]
lst_2 = [3,5,6]

print(merge(lst_1,lst_2))

print(merge_sort(list))

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1)
print(ordered_list2)
print(ordered_list3)