def merge_sort(arr):
    if(len(arr) == 1):
        return arr
    else:
        middle = len(arr) //2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)
        return merge(left_arr,right_arr)
    
def merge(left_arr, right_arr):
    sorted_arr = []
    left_index = 0
    right_index = 0
    while (left_index < len(left_arr) and right_index < len(right_arr)):
        if(left_arr[left_index] < right_arr[right_index]):
            sorted_arr.append(left_arr[left_index])
            left_index+=1
        else :
            sorted_arr.append(right_arr[right_index])
            right_index +=1

    sorted_arr += left_arr[left_index:]
    sorted_arr += right_arr[right_index:]
    return sorted_arr    