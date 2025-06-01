def bubble_sort(arr):
    n=len(arr)
    for i in range (n):
        swapped=False           #Track if swap occured in this pass
        for j in range(n-i-1):  #reduce camparison length by 1 after each iteration
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
         break              #if no swap occurs,the list is already sorted

numbers=[50,20,40,10,30]
bubble_sort(numbers)
print(f"Sorted list:{numbers}")