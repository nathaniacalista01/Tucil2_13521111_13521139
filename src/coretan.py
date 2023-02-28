#Cuma alternatif algoritma doank
#Algoritma untuk sort berdasarkan dimension (misalnya mau sort based on dimesi Y atau Z)
def merge_sort2(arr,dimension):
    if(len(arr) == 1):
        return arr
    else:
        middle = len(arr) //2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        left_arr = merge_sort2(left_arr,dimension)
        right_arr = merge_sort2(right_arr,dimension)
        return merge2(left_arr,right_arr,dimension)
    
def merge2(left_arr,right_arr, dimension):
    sorted_arr = []
    left = 0
    right = 0
    while(left < len(left_arr) and right < len(right_arr)):
        if(left_arr[left][dimension] < right_arr[right][dimension]):
            sorted_arr.append(left_arr[left])
            left += 1
        else : 
            sorted_arr.append(right_arr[right])
            right += 1
    sorted_arr += left_arr[left:]
    sorted_arr += right_arr[right:]
    return sorted_arr

