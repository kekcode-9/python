#Given two lists, check if they are identical. Lists are identical if after sorting both lists have the same values with the same frequency.
#Swap elements to distribute them evenly. Each swapping has a cost equal to the value of the smaller of the two items being swapped. If the lists
#are identical then return the total cost. If they cannot be made identical then return -1
def findCost():
	N = int(input())
	A = []
	B = []
	cost = [0]
	def do(w):
		wcountA = A.count(w)
		wcountB = B.count(w)
		if(wcountA!=0 and wcountB!=0):
			wfirstA = A.index(w)
			wfirstB = B.index(w)
			diff = wcountA - wcountB
			if(diff>0):
				wdeltillA = wfirstA + wcountB
				wdeltillB = wfirstB + wcountB
			elif(diff<0):
				wdeltillA = wfirstA + wcountA
				wdeltillB = wfirstB + wcountA
			else:
				wdeltillA = wfirstA + wcountA
				wdeltillB = wfirstB + wcountB
			del A[wfirstA:wdeltillA]
			del B[wfirstB:wdeltillB]
		wcountA = A.count(w)
		wcountB = B.count(w)
		if(wcountA>0):
			wfirstA = A.index(w)
			rem = wcountA%2
			half = int(wcountA/2)
			if(rem==0):
				wdeltillA = wfirstA + half
				del A[wfirstA:wdeltillA]
			else:
				cost[0] = -1
		elif(wcountB>0):
			wfirstB = B.index(w)
			rem = wcountB%2
			half = int(wcountB/2)
			if(rem==0):
				wdeltillB = wfirstB + half
				del B[wfirstB:wdeltillB]
			else:
				cost[0] = -1
				
	A = list(map(int,input().split(" ")))
	A.sort()
	B = list(map(int,input().split(" ")))
	B.sort()
	if(A==B):
		return 0
	A1 = A.copy()
	B1 = B.copy()
	l1 = A1+B1
	l1 = list(set(l1))
	l1.sort()
	[do(x) for x in l1 if(cost[0]!=-1)]
	if(cost[0]==-1):
		return -1
	l = len(A)
	A.sort()
	B.sort()
	def swap():
		a = int(A[0])
		b = int(B[-1])
		cost[0] = cost[0] + min(a,b)
		A.pop(0)
		B.pop(-1)
	map(lambda x: swap(), range(l))
	return cost[0]

if __name__=='__main__':
	testcases = int(input())
	costs = [findCost() for i in range(testcases)]
	print(*costs,sep="\n")
