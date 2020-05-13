from functools import reduce
def merge_the_tools(str1, k):
	def removeRepeates(str2):
		k=len(str2);
		#list comprehension to obtain a list of letters from the string
		list1=[str2[i] for i in range(0,k)]
		#put  list1[i]  in list2 only if list1[i] hasn't occured once in list[0:i]
		list2=[list1[i] for i in range(0,k) if list1[0:i].count(list1[i])==0]
		#reduce the elements of list2 into a string
		str2=reduce(lambda letter1, letter2: letter1+letter2, list2)
		return str2

	n= len(str1)/k
	#list comprehension to split string into a list of strings each of length k
	list1=[str1[i:i+k] for i in range(0,len(str1),k)]
	#print(list1)
	list2=list(map(removeRepeates,list1))
	for item in list2:
		print(item)
	 

if __name__ == '__main__':
	str1=input("enter the string: ")
	k=int(input("enter k: "))
	merge_the_tools(str1, k)
    