class node(object):
	"""docstring for node"""
	def __init__(self, val):
		
		self.value = val
		self.count = 1
		self.left = None
		self.right = None


def insert(root,val):
	
	if root.value == val:
		root.count+=1
		
	elif root.value > val:
		if root.left == None:
			root.left = node(val)
		else :
			insert(root.left,val)
	else :
		if root.right == None:
			root.right = node(val)
		else:
			insert(root.right,val)

	return root


def inorder(node):
	if node != None:
		inorder(node.left)
		for i in xrange(node.count):
			print node.value,
		inorder(node.right)

a= "5 4 8 63 2 58 2 25 5 5 1 4 1 2 5 5 22 63 3 3 25 3 3 5"
a = map(int,a.split())
print len(a)
root = None

for e in a:
	if root == None:
		root = node(e)
	else:
		insert(root,e)

inorder(root)
