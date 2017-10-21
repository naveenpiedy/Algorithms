import math
def MergeSort(unsorted_list):
    if len(unsorted_list) > 1:
        left_half = unsorted_list[: math.floor(len(unsorted_list)/2)]
        right_half = unsorted_list[math.floor(len(unsorted_list)/2):]
        MergeSort(left_half)
        MergeSort(right_half)
        i, j, k = 0,0,0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                unsorted_list[k] = left_half[i]
                i+=1
            else:
                unsorted_list[k] = right_half[j]
                j+=j+1
            k+=1
        if i< len(left_half):
            unsorted_list[k:] = left_half[i:]
        if j < len(right_half):
            unsorted_list[k:]= right_half[j:]
    return unsorted_list


# def main():
#     s = MergeSort([5,56,8,65,2,56,56,4564])
#     print(s)
# if __name__ == '__main__':
#     main()