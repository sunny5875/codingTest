array = [3,4,2,5,6,1,8,10]

def quick_sort(array,start,end):
    if start>= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left +=1
        while right > start and array[right] >= array[pivot]:
            right -=1
        
        if left > right: #엇갈렸으면 Pivot과 right swap
            array[right], array[pivot] = array[pivot], array[right]
        else: #맞다면 left, right를 변경
             array[right], array[left] = array[left], array[right]
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array) -1 )
print(array)

array1 = [3,4,2,5,6,1,8,10]
##### sortcut version #####
def quick_sort(array):
    if len(array) == 0:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array1))