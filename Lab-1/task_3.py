numbers = list(map(int, input().split(",")))

def bubble_sort(arr):
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
                swapped = True
        if swapped == False:
            break
    return sorted_arr

def gnome_sort(arr):
    sorted_arr = arr.copy()
    i = 0
    while i < len(sorted_arr):
        if i == 0:
            i += 1
        if sorted_arr[i] >= sorted_arr[i - 1]:
            i += 1
        else:
            sorted_arr[i], sorted_arr[i-1] = sorted_arr[i-1], sorted_arr[i]
            i -= 1
    return sorted_arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1 # left
    r = 2 * i + 2 # right
 
    # if left child > root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # if right child > root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    # building a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(sorted_arr, n, i)

    # extracting elements
    for i in range(n - 1, 0, -1):
        sorted_arr[i], sorted_arr[0] = sorted_arr[0], sorted_arr[i]
        heapify(sorted_arr, i, 0)

    return sorted_arr

def bucket_sort(arr, n):
    s_arr = arr.copy()
    max_ele = max(s_arr)
    min_ele = min(s_arr)
 
    # range(for buckets)
    rnge = (max_ele - min_ele) / n
 
    temp = []
 
    # create empty buckets
    for i in range(n):
        temp.append([])
 
    for i in range(len(s_arr)):
        diff = (s_arr[i] - min_ele) / rnge - int((s_arr[i] - min_ele) / rnge)

        if diff == 0 and s_arr[i] != min_ele:
            temp[int((s_arr[i] - min_ele) / rnge) - 1].append(s_arr[i])
        else:
            temp[int((s_arr[i] - min_ele) / rnge)].append(s_arr[i])
 
    # sorting each bucket
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
    
    # creating sorted array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                s_arr[k] = i
                k = k+1
    
    return s_arr

print(bubble_sort(numbers))
print(gnome_sort(numbers))
print(heap_sort(numbers))
print(bucket_sort(numbers, len(numbers) // 2))
print(numbers)