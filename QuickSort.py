def QuickSort(unsorted_list):
    #print(unsorted_list)
    if unsorted_list:
        pivot = unsorted_list[0]
        pivot_index = 0
        for i in range(0, len(unsorted_list)):
            #pivot_index = unsorted_list.index(pivot)
            if unsorted_list[i] < pivot:
                temp = unsorted_list[i]
                unsorted_list[pivot_index+1:i+1] = unsorted_list[pivot_index:i]
                unsorted_list[pivot_index] = temp
                pivot_index = unsorted_list.index(pivot)
        if unsorted_list[:pivot_index] is not None:
            #print("Sending Leftside", unsorted_list[:pivot_index])
            unsorted_list[:pivot_index] = QuickSort(unsorted_list[:pivot_index])
        if len(unsorted_list[pivot_index + 1:]) > 1:
            #print("Sending Rightside", unsorted_list[pivot_index+1:])
            unsorted_list[pivot_index + 1:] = QuickSort(unsorted_list[pivot_index + 1:])
        return unsorted_list
    else:
        return unsorted_list

# def listarray(k):
#     k[0] = k[1]
#     print(k)
#
# def main():
#     s = QuickSort([5,2,3,65,2,56,56,4564])
#     print(s)
# if __name__ == '__main__':
#     main()