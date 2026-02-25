def selection_sort(li):
    n = len(li)
    for i in range(n-1):
        min_index=i
        for j in range (i+1, n):
            if li[j] < li[min_index]:
                min_index = j
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]
    return li

li=[5,2,8,3,4,6,100,3,7]
print(f"The list before sorting:{li}")

print(f"The list after sorting: {selection_sort(li)}")