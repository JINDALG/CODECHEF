# Article link- http://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
# Python program to show segment tree operations like construction, query
# and update

import math
# A utility function to get the middle index from corner indexes.
def getmid(a,b):
	return a+(b-a)/2

def update(st,ss,se,val,ind,si):
	# if segment index at leaf node level
	# update the node value and return
	if ss == se:
		st[si] += val
		return
	else :
		# If the input index is in range of this node, then update 
  		# the value of the node and its children
		st[si] += val
		mid = getmid(ss,se)
		if ind <= mid:
			update(st,ss,mid,val,ind,si*2+1)
		else :
			update(st,mid+1,se,val,ind,si*2+2)
# The function to update a value in input array and segment tree.
# It uses update() to update the value in segment tree
def updatest(st,a,l,val,ind):
	# Get the difference between new value and old value
	diff = val-a[ind]
	# Update the values of nodes in segment tree
	update(st,0,len(st)/2,diff,ind,0)


def minquery(st,ss,se,qs,qe,si):
	# If segment of this node is outside the given range return vary high value
	if se<qs or ss>qe:
		return 999999
	# If segment of this node is a part of given range, then return
 	# the sum of the segment
	elif qs<=ss and qe>=se : 
		return st[si]
	else :
		# If a part of this segment overlaps with the given range
		mid = getmid(ss,se)
		return min(minquery(st,ss,mid,qs,qe,si*2+1),minquery(st,mid+1,se,qs,qe,si*2+2))


# Function to construct segment tree from given array.
# A recursive function that constructs Segment Tree for array[0..l-1].
def create_tree(a,l):
	# Maximum size of segment tree
	size = 2*pow(2,int(math.ceil(math.log(l,2))))-1
	# initialize segment tree array with all element have very high (infine) value
	st = [99999999]*size
	j = 0
	# Fill the array element at leaf node level of segment tree
	for i in xrange(size/2,size/2+l):
		st[i] = a[j]
		j+=1
	i = size/2-1
	# Set value of all internal node with the sum of left and right subtree
	while i >= 0:
		st[i] = min(st[2*i+1],st[2*i+2])
		i-=1
	# return segment tree
	return st

# Driver program to test above functions
def main():
	a = [1,3,2,7,9,11,9,3]
	l = len(a)
	# Build segment tree from given array
	st = create_tree(a[:],l)
	# Print minimum value in arr[1..3]
	print  "Minimum of values in given range = %d" %RMQ(st,len(st)/2,1,3)

	# Update: set arr[1] = 10 and update corresponding segment tree nodes
	updatest(st,a,l,1,2)
	
	# Print minimum value in arr[1..3]
	print "Updated Minimum of values in given range = %d" %RMQ(st,0,len(st)/2,1,3,0)


main()

# time complexity for update and minquery in logN