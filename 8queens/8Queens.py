def isSafe(r2, c2):
	for r1 in range(1, r2):
		c1 = C[r1]
		if ((c1 == c2) or (abs(r1-r2) == abs(c1-c2))):
			return False
	return True

def n_queens(C, r):
	if(r == n-1):
		print(C)
		return True
	for c in range(1, n+1):
		fin = False
		if(isSafe(r+1,c)):
			C[r+1] = c
			fin = n_queens(C, r+1)
	return fin
				
				

n = int(input("Enter the number of queens : "))
C = [0 for x in range(n)]
n_queens(C, 0)



'''
Output:
Enter the number of queens : 8
[0, 1, 3, 5, 7, 2, 4, 6]
[0, 1, 3, 5, 8, 2, 4, 6]
[0, 1, 3, 8, 6, 4, 2, 5]
[0, 1, 4, 6, 8, 2, 5, 3]
[0, 1, 4, 6, 8, 2, 7, 3]
[0, 1, 4, 7, 3, 6, 2, 5]
[0, 1, 4, 7, 3, 8, 2, 5]
[0, 1, 5, 2, 6, 3, 7, 4]
[0, 1, 5, 2, 8, 3, 7, 4]
[0, 1, 5, 8, 2, 4, 7, 3]
[0, 1, 5, 8, 2, 7, 3, 6]
[0, 1, 5, 8, 6, 3, 7, 2]
[0, 1, 6, 4, 2, 7, 5, 3]
[0, 1, 6, 4, 2, 8, 5, 3]
[0, 1, 6, 8, 2, 4, 7, 3]
[0, 1, 6, 8, 3, 7, 4, 2]
[0, 1, 7, 4, 2, 8, 5, 3]
[0, 1, 7, 4, 6, 8, 2, 5]
[0, 1, 7, 5, 8, 2, 4, 6]
[0, 1, 8, 4, 2, 7, 3, 6]
[0, 1, 8, 6, 3, 7, 2, 4]
[0, 2, 4, 1, 7, 5, 3, 6]
[0, 2, 4, 1, 8, 5, 3, 6]
[0, 2, 4, 6, 1, 3, 5, 7]
[0, 2, 4, 6, 8, 3, 1, 7]
[0, 2, 4, 6, 8, 3, 5, 7]
[0, 2, 4, 7, 3, 8, 6, 1]
[0, 2, 5, 1, 4, 7, 3, 6]
[0, 2, 5, 3, 1, 7, 4, 6]
[0, 2, 5, 7, 1, 3, 8, 6]
[0, 2, 5, 7, 4, 1, 3, 6]
[0, 2, 5, 7, 4, 1, 8, 6]
[0, 2, 5, 8, 1, 4, 6, 3]
[0, 2, 5, 8, 1, 7, 4, 6]
[0, 2, 5, 8, 4, 1, 3, 6]
[0, 2, 5, 8, 4, 7, 3, 6]
[0, 2, 5, 8, 6, 1, 3, 7]
[0, 2, 6, 1, 3, 5, 8, 4]
[0, 2, 6, 1, 7, 4, 8, 3]
[0, 2, 6, 3, 1, 4, 8, 5]
[0, 2, 6, 3, 7, 4, 1, 5]
[0, 2, 6, 3, 7, 4, 8, 5]
[0, 2, 6, 8, 3, 1, 4, 7]
[0, 2, 7, 1, 3, 5, 8, 4]
[0, 2, 7, 1, 3, 8, 6, 4]
[0, 2, 7, 1, 4, 8, 5, 3]
[0, 2, 7, 3, 6, 8, 1, 4]
[0, 2, 7, 3, 6, 8, 1, 5]
[0, 2, 7, 3, 6, 8, 5, 1]
[0, 2, 7, 5, 1, 8, 6, 3]
[0, 2, 7, 5, 3, 1, 6, 4]
[0, 2, 7, 5, 3, 8, 6, 4]
[0, 2, 7, 5, 8, 1, 4, 6]
[0, 2, 8, 1, 4, 7, 3, 6]
[0, 2, 8, 3, 7, 4, 1, 5]
[0, 2, 8, 5, 3, 1, 6, 4]
[0, 2, 8, 5, 7, 1, 3, 6]
[0, 2, 8, 6, 1, 3, 5, 7]
[0, 3, 1, 6, 2, 5, 7, 4]
[0, 3, 1, 6, 4, 2, 7, 5]
[0, 3, 1, 6, 8, 2, 4, 7]
[0, 3, 1, 6, 8, 5, 2, 4]
[0, 3, 1, 6, 8, 5, 7, 4]
[0, 3, 1, 7, 2, 8, 6, 4]
[0, 3, 1, 7, 5, 8, 2, 4]
[0, 3, 1, 7, 5, 8, 6, 4]
[0, 3, 1, 8, 4, 2, 7, 5]
[0, 3, 1, 8, 5, 2, 4, 7]
[0, 3, 5, 2, 8, 1, 4, 7]
[0, 3, 5, 2, 8, 1, 7, 4]
[0, 3, 5, 2, 8, 6, 4, 1]
[0, 3, 5, 2, 8, 6, 4, 7]
[0, 3, 5, 7, 1, 4, 2, 8]
[0, 3, 5, 7, 1, 4, 6, 8]
[0, 3, 5, 7, 2, 4, 6, 1]
[0, 3, 5, 7, 2, 4, 6, 8]
[0, 3, 5, 8, 1, 4, 2, 7]
[0, 3, 5, 8, 2, 4, 6, 1]
[0, 3, 5, 8, 2, 4, 7, 1]
[0, 3, 5, 8, 4, 1, 7, 2]
[0, 3, 6, 2, 5, 1, 4, 7]
[0, 3, 6, 2, 5, 8, 1, 4]
[0, 3, 6, 2, 5, 8, 1, 7]
[0, 3, 6, 2, 5, 8, 4, 7]
[0, 3, 6, 2, 7, 1, 4, 8]
[0, 3, 6, 2, 7, 5, 1, 8]
[0, 3, 6, 4, 1, 8, 5, 2]
[0, 3, 6, 4, 1, 8, 5, 7]
[0, 3, 6, 4, 2, 8, 5, 7]
[0, 3, 6, 8, 1, 4, 7, 5]
[0, 3, 6, 8, 1, 5, 7, 2]
[0, 3, 6, 8, 2, 4, 1, 7]
[0, 3, 6, 8, 5, 1, 4, 7]
[0, 3, 6, 8, 5, 2, 4, 7]
[0, 3, 7, 2, 4, 6, 1, 5]
[0, 3, 7, 2, 4, 8, 1, 5]
[0, 3, 7, 2, 8, 5, 1, 4]
[0, 3, 7, 2, 8, 6, 4, 1]
[0, 3, 7, 4, 1, 5, 2, 6]
[0, 3, 7, 4, 1, 8, 2, 5]
[0, 3, 7, 4, 2, 8, 5, 1]
[0, 3, 7, 4, 2, 8, 6, 1]
[0, 3, 7, 4, 8, 5, 2, 6]
[0, 3, 8, 2, 4, 1, 7, 5]
[0, 3, 8, 2, 4, 6, 1, 5]
[0, 3, 8, 2, 5, 1, 6, 4]
[0, 3, 8, 4, 7, 1, 6, 2]
[0, 3, 8, 6, 4, 1, 7, 5]
[0, 3, 8, 6, 4, 2, 7, 5]
[0, 4, 1, 3, 6, 2, 7, 5]
[0, 4, 1, 5, 2, 6, 3, 7]
[0, 4, 1, 5, 8, 2, 7, 3]
[0, 4, 1, 5, 8, 6, 3, 7]
[0, 4, 1, 8, 5, 2, 6, 3]
[0, 4, 1, 8, 6, 2, 7, 5]
[0, 4, 1, 8, 6, 3, 7, 2]
[0, 4, 2, 5, 8, 1, 3, 6]
[0, 4, 2, 5, 8, 6, 1, 3]
[0, 4, 2, 7, 3, 1, 8, 5]
[0, 4, 2, 7, 3, 6, 8, 1]
[0, 4, 2, 7, 3, 6, 8, 5]
[0, 4, 2, 7, 5, 1, 8, 6]
[0, 4, 2, 7, 5, 3, 1, 6]
[0, 4, 2, 7, 5, 3, 8, 6]
[0, 4, 2, 8, 3, 1, 7, 5]
[0, 4, 2, 8, 5, 3, 1, 6]
[0, 4, 2, 8, 5, 7, 1, 3]
[0, 4, 2, 8, 5, 7, 1, 6]
[0, 4, 2, 8, 6, 1, 3, 5]
[0, 4, 2, 8, 6, 1, 7, 5]
[0, 4, 6, 1, 3, 5, 7, 2]
[0, 4, 6, 1, 3, 5, 8, 2]
[0, 4, 6, 1, 5, 2, 8, 3]
[0, 4, 6, 8, 2, 7, 1, 3]
[0, 4, 6, 8, 3, 1, 7, 2]
[0, 4, 6, 8, 3, 1, 7, 5]
[0, 4, 6, 8, 3, 5, 7, 2]
[0, 4, 6, 8, 5, 7, 1, 3]
[0, 4, 7, 1, 3, 5, 2, 8]
[0, 4, 7, 1, 6, 2, 5, 8]
[0, 4, 7, 1, 8, 2, 5, 3]
[0, 4, 7, 1, 8, 5, 2, 6]
[0, 4, 7, 3, 6, 2, 5, 1]
[0, 4, 7, 3, 6, 2, 5, 8]
[0, 4, 7, 3, 8, 2, 5, 1]
[0, 4, 7, 5, 2, 6, 1, 3]
[0, 4, 7, 5, 3, 1, 6, 8]
[0, 4, 7, 5, 8, 6, 1, 3]
[0, 4, 8, 1, 3, 6, 2, 7]
[0, 4, 8, 1, 5, 7, 2, 6]
[0, 4, 8, 3, 5, 7, 1, 6]
[0, 4, 8, 3, 5, 7, 2, 6]
[0, 4, 8, 5, 2, 6, 1, 7]
[0, 4, 8, 5, 2, 6, 3, 7]
[0, 4, 8, 5, 3, 1, 6, 2]
[0, 4, 8, 5, 3, 1, 7, 2]
[0, 5, 1, 4, 6, 8, 2, 7]
[0, 5, 1, 4, 6, 8, 3, 7]
[0, 5, 1, 4, 7, 3, 6, 2]
[0, 5, 1, 4, 7, 3, 8, 2]
[0, 5, 1, 6, 4, 2, 7, 3]
[0, 5, 1, 6, 4, 2, 8, 3]
[0, 5, 1, 8, 4, 2, 7, 3]
[0, 5, 1, 8, 6, 3, 7, 2]
[0, 5, 2, 4, 1, 3, 8, 6]
[0, 5, 2, 4, 6, 8, 3, 1]
[0, 5, 2, 4, 7, 3, 8, 6]
[0, 5, 2, 6, 1, 7, 4, 8]
[0, 5, 2, 6, 3, 7, 4, 1]
[0, 5, 2, 6, 3, 7, 4, 8]
[0, 5, 2, 8, 1, 4, 7, 3]
[0, 5, 2, 8, 1, 7, 4, 6]
[0, 5, 2, 8, 3, 7, 4, 1]
[0, 5, 2, 8, 6, 4, 7, 1]
[0, 5, 3, 1, 4, 2, 8, 6]
[0, 5, 3, 1, 6, 4, 2, 7]
[0, 5, 3, 1, 6, 8, 2, 4]
[0, 5, 3, 1, 6, 8, 2, 7]
[0, 5, 3, 1, 7, 2, 8, 6]
[0, 5, 3, 8, 4, 7, 1, 6]
[0, 5, 3, 8, 6, 4, 1, 7]
[0, 5, 3, 8, 6, 4, 2, 7]
[0, 5, 7, 1, 3, 8, 2, 4]
[0, 5, 7, 1, 3, 8, 6, 4]
[0, 5, 7, 1, 4, 2, 8, 3]
[0, 5, 7, 1, 4, 2, 8, 6]
[0, 5, 7, 1, 4, 6, 8, 3]
[0, 5, 7, 1, 6, 8, 2, 4]
[0, 5, 7, 2, 4, 6, 1, 3]
[0, 5, 7, 2, 4, 6, 8, 3]
[0, 5, 7, 2, 4, 8, 1, 3]
[0, 5, 7, 2, 6, 3, 1, 4]
[0, 5, 7, 2, 6, 3, 1, 8]
[0, 5, 7, 2, 6, 8, 1, 4]
[0, 5, 7, 4, 1, 3, 8, 6]
[0, 5, 7, 4, 1, 8, 6, 3]
[0, 5, 8, 1, 3, 6, 2, 7]
[0, 5, 8, 1, 3, 7, 2, 4]
[0, 5, 8, 1, 4, 7, 3, 6]
[0, 5, 8, 4, 1, 3, 6, 2]
[0, 5, 8, 4, 1, 7, 2, 6]
[0, 5, 8, 4, 7, 3, 6, 2]
[0, 5, 8, 6, 3, 7, 2, 4]
[0, 6, 1, 3, 5, 7, 2, 4]
[0, 6, 1, 3, 5, 8, 2, 4]
[0, 6, 1, 5, 2, 8, 3, 7]
[0, 6, 1, 7, 4, 8, 3, 5]
[0, 6, 1, 7, 5, 3, 8, 4]
[0, 6, 1, 7, 5, 8, 2, 4]
[0, 6, 2, 5, 1, 4, 7, 3]
[0, 6, 2, 5, 7, 1, 3, 8]
[0, 6, 2, 5, 7, 1, 4, 8]
[0, 6, 2, 5, 8, 1, 7, 4]
[0, 6, 2, 5, 8, 4, 7, 3]
[0, 6, 2, 7, 1, 3, 5, 8]
[0, 6, 2, 7, 1, 4, 8, 5]
[0, 6, 2, 7, 5, 1, 8, 4]
[0, 6, 2, 7, 5, 3, 8, 4]
[0, 6, 3, 1, 4, 7, 5, 2]
[0, 6, 3, 1, 4, 8, 5, 2]
[0, 6, 3, 1, 7, 5, 8, 2]
[0, 6, 3, 1, 8, 4, 2, 7]
[0, 6, 3, 1, 8, 5, 2, 4]
[0, 6, 3, 5, 7, 1, 4, 2]
[0, 6, 3, 5, 8, 1, 4, 2]
[0, 6, 3, 5, 8, 1, 4, 7]
[0, 6, 3, 7, 2, 4, 8, 1]
[0, 6, 3, 7, 2, 8, 5, 1]
[0, 6, 3, 7, 4, 1, 5, 2]
[0, 6, 3, 7, 4, 1, 8, 2]
[0, 6, 3, 7, 4, 1, 8, 5]
[0, 6, 3, 7, 4, 8, 5, 2]
[0, 6, 4, 1, 5, 8, 2, 7]
[0, 6, 4, 1, 7, 5, 2, 8]
[0, 6, 4, 1, 7, 5, 3, 8]
[0, 6, 4, 1, 8, 5, 7, 2]
[0, 6, 4, 2, 7, 5, 3, 1]
[0, 6, 4, 2, 7, 5, 3, 8]
[0, 6, 4, 2, 8, 5, 3, 1]
[0, 6, 4, 2, 8, 5, 7, 1]
[0, 6, 4, 7, 1, 3, 5, 2]
[0, 6, 4, 7, 1, 3, 5, 8]
[0, 6, 4, 7, 1, 8, 2, 5]
[0, 6, 4, 7, 1, 8, 5, 2]
[0, 6, 8, 1, 4, 7, 5, 2]
[0, 6, 8, 1, 5, 7, 2, 4]
[0, 6, 8, 2, 4, 1, 3, 5]
[0, 6, 8, 2, 4, 1, 7, 5]
[0, 6, 8, 2, 7, 1, 3, 5]
[0, 6, 8, 3, 1, 4, 2, 5]
[0, 6, 8, 3, 1, 4, 7, 5]
[0, 6, 8, 3, 1, 7, 5, 2]
[0, 6, 8, 3, 5, 7, 2, 4]
[0, 6, 8, 3, 7, 4, 2, 5]
[0, 7, 1, 3, 8, 6, 4, 2]
[0, 7, 1, 4, 2, 8, 6, 3]
[0, 7, 1, 4, 6, 8, 3, 5]
[0, 7, 1, 6, 2, 5, 8, 4]
[0, 7, 1, 8, 5, 2, 6, 3]
[0, 7, 2, 4, 1, 8, 5, 3]
[0, 7, 2, 4, 6, 1, 3, 5]
[0, 7, 2, 4, 6, 8, 3, 5]
[0, 7, 2, 4, 8, 1, 3, 6]
[0, 7, 2, 6, 3, 1, 4, 8]
[0, 7, 2, 6, 3, 1, 8, 4]
[0, 7, 2, 6, 3, 1, 8, 5]
[0, 7, 2, 8, 5, 1, 4, 6]
[0, 7, 2, 8, 6, 1, 3, 5]
[0, 7, 2, 8, 6, 4, 1, 5]
[0, 7, 3, 1, 6, 8, 5, 2]
[0, 7, 3, 6, 2, 5, 1, 4]
[0, 7, 3, 6, 2, 5, 8, 4]
[0, 7, 3, 6, 8, 5, 1, 4]
[0, 7, 3, 8, 2, 5, 1, 6]
[0, 7, 3, 8, 6, 4, 1, 5]
[0, 7, 4, 1, 3, 8, 6, 2]
[0, 7, 4, 1, 5, 2, 6, 3]
[0, 7, 4, 1, 5, 8, 6, 3]
[0, 7, 4, 1, 8, 2, 5, 3]
[0, 7, 4, 1, 8, 5, 3, 6]
[0, 7, 4, 2, 5, 8, 1, 3]
[0, 7, 4, 2, 5, 8, 6, 3]
[0, 7, 4, 2, 8, 6, 1, 3]
[0, 7, 4, 6, 8, 2, 5, 3]
[0, 7, 4, 8, 5, 2, 6, 3]
[0, 7, 5, 2, 6, 1, 3, 8]
[0, 7, 5, 3, 1, 6, 4, 2]
[0, 7, 5, 3, 1, 6, 8, 2]
[0, 7, 5, 3, 8, 6, 4, 2]
[0, 7, 5, 8, 1, 4, 6, 3]
[0, 7, 5, 8, 2, 4, 6, 3]
[0, 8, 1, 3, 6, 2, 7, 5]
[0, 8, 1, 5, 7, 2, 6, 3]
[0, 8, 2, 4, 1, 7, 5, 3]
[0, 8, 2, 5, 3, 1, 7, 4]
[0, 8, 2, 5, 7, 1, 4, 6]
[0, 8, 3, 1, 6, 2, 5, 7]
[0, 8, 3, 1, 7, 5, 2, 6]
[0, 8, 3, 5, 7, 1, 4, 6]
[0, 8, 3, 5, 7, 2, 4, 6]
[0, 8, 4, 1, 3, 6, 2, 7]
[0, 8, 4, 1, 7, 2, 6, 3]
[0, 8, 4, 1, 7, 5, 2, 6]
[0, 8, 4, 7, 1, 6, 2, 5]
[0, 8, 4, 7, 3, 6, 2, 5]
[0, 8, 5, 2, 6, 1, 7, 4]
[0, 8, 5, 2, 6, 3, 7, 4]
[0, 8, 5, 3, 1, 7, 2, 6]
[0, 8, 5, 3, 1, 7, 4, 6]
[0, 8, 6, 1, 3, 5, 7, 4]
[0, 8, 6, 4, 1, 7, 5, 3]
[0, 8, 6, 4, 2, 7, 5, 3]

'''
