
#usr/bin/python3



def quicksort(arr, start, end):
    if start < end:
        pIndex = partition2(arr, start, end)
        quicksort(arr, start, pIndex - 1)
        quicksort(arr, pIndex + 1, end)
    return arr
def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end - 1):
        if (arr[i] <= pivot):
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
        print(arr[i])
    arr[pIndex], arr[end] = arr[end], arr[pIndex]

    return pIndex

def partition2(a, start, end): 
    """partition de las clases yadran"""
    pIndex = start - 1
    k = end
    pivot = a[end]

    while True:
        pIndex +=1
        while a[pIndex] < pivot:
            pIndex += 1
        k -= 1
        while a[k] < pivot:
            k -= 1
            if k == start:
                break
        if pIndex >= k:
            break
        a[pIndex], a[k] = a[k], a[pIndex]
    a[pIndex], a[end] = a[end], a[pIndex]
    return pIndex


a = [1,4,3,5,5,7]
end = len(a) - 1
start = 0

quicksort(a, start, end)
print(a)

