import math

def getmid(a,b):
	return a+(b-a)/2

def update(st,ss,se,val,ind,si):
	if ss == se:
		st[si] += val
		return
	else :
		st[si] += val
		mid = getmid(ss,se)
		if ind <= mid:
			update(st,ss,mid,val,ind,si*2+1)
		else :
			update(st,mid+1,se,val,ind,si*2+2)


def getsum(st,ss,se,qs,qe,si):
	if se<qs or ss>qe:
		return 0 
	elif qs<=ss and qe>=se : 
		return st[si]
	else :
		mid = getmid(ss,se)
		return getsum(st,ss,mid,qs,qe,si*2+1) + getsum(st,mid+1,se,qs,qe,si*2+2)
		 
def create_tree(a,l):
	size = 2*pow(2,int(math.ceil(math.log(l,2))))-1
	st = [0]*size
	j = 0
	for i in xrange(size/2,size/2+l):
		st[i] = a[j]
		j+=1
	i = size/2-1
	while i >= 0:
		st[i] = st[2*i+1] + st[2*i+2]
		i-=1
	return st

def main():
	a = [5,4,1,2,6,8]
	l = len(a)
	st = create_tree(a[:],l)
	print "initial segment tree"
	print st
	ind = 2 # index of array at which value have to update
	val = 5 # value increase at index ind

	update(st,0,len(st)/2,val,ind,0)
	print "segment tree after upadte value of a[%d]" %ind
	print st
	print "sum of index from %d to %d after update" %(0,7)
	print getsum(st,0,len(st)/2,0,7,0)


main()