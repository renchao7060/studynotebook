def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

if __name__=='__main__':
    bubbleSort([10,8,1,5,7,12,3])
