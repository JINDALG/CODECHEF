# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

def count(arr, m, n):
	table = [[0 for j in xrange(m)] for i in xrange(n+1)]

	# if n == 0 then there will be only one solution
	for i in xrange(m):
		table[0][i] = 1

	for i in xrange(1,n+1):
		for j in xrange(m):

			# count by including of arr[j] coin
			x = table[i-arr[j]][j] if (i-arr[j] >= 0) else 0

			# count by excluding of arr[j] coin
			y = table[i][j-1] if (j >= 1) else 0

			table[i][j] = x + y

	return table[n][m-1]


def main():
	arr = [2, 6, 3, 5]
	l = len(arr)
	money = 10
	print count(arr, l, money)

main()