def Merge (left,right,merged):
    #Ф-ция объединения и сравнения элементов массивов 
    left_cursor,right_cursor=0,0
    while left_cursor<len(left) and right_cursor<len(right):
        if left[left_cursor]<=right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor+=1
        else:
            merged[left_cursor+right_cursor]=right[right_cursor]
            right_cursor+=1
    for left_cursor in range(left_cursor,len(left)):
        merged[left_cursor+right_cursor]=left[left_cursor]
    for right_cursor in range(right_cursor,len(right)):
         merged[left_cursor+right_cursor]=right[right_cursor]
    return merged

def MergeSort(array):
    #Основная рекурсивная функция
    if len(array)<=1:
        return array
    mid=len(array)//2
    left,right=MergeSort(array[:mid]),MergeSort(array[mid:])
    return Merge(left,right,array.copy())


"""
a=[2,45,1,4,66,34]
print(MergeSort(a))
print(a) 
"""
