def quickSort(low,high,kindex,arr):
	if(low<high):
		pivot_index=partition(low,high,arr)
		if(kindex>pivot_index):
			quickSort(pivot_index+1,high,kindex,arr)
		elif(kindex<pivot_index):
			quickSort(low,pivot_index-1,kindex,arr)
		else:
			return

def partition(low,high,arr):
	x=round((low+high-1)/2)
	arr[low], arr[x]= arr[x], arr[low]
	pivot= arr[low]
	last_small=low
	for i in range(low,high+1,1):
		if(arr[i]<pivot):
			last_small=last_small+1
			arr[last_small], arr[i]= arr[i], arr[last_small]
	arr[low], arr[last_small]= arr[last_small], arr[low]
	return last_small

if __name__ == '__main__':
    print ("Find Kth largest element in an array")
    n = int(input())
    arr = []
    for i in range(n):
    	arr.append(int(input(": ")))
    print ("arr: ", arr)
    k= int(input("Enter K: "))
    arr=list(dict.fromkeys(arr)) #removing duplicates by creating dictionary with arr elements as index
    n=len(arr)
    kindex=n-k
    quickSort(0,n-1,kindex,arr)
    print("the ",k,"'th largest element is ",arr[kindex])