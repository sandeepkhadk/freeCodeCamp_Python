def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    arr1 = []
    arr2 = []
    arr3 = []

    for i in arr:
        if i < pivot:
            arr1.append(i)
        elif i == pivot:
            arr2.append(i)
        else:
            arr3.append(i)

    a = quick_sort(arr1)
    c = quick_sort(arr3)

    return a + arr2 + c

li=[5,2,8,3,4,6,100,3,7]
print(f"The list before sorting:{li}")

print(f"The list after sorting: {quick_sort(li)}")