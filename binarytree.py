class node(object):
	"""docstring for ClassName"""
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

def inorder(node):
	if node != None:
		inorder(node.left)
		print node.value,
		inorder(node.right)
	
def preorder(node):
	if node != None:
		print node.value,
		preorder(node.left)
		preorder(node.right)

def postorder(node):
	if node != None:
		postorder(node.left)
		postorder(node.right)
		print node.value,

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(8)


print "preorder is :"
preorder(root)
print
print "inorder is :"
inorder(root)
print 
print "postorder is :"
postorder(root)
print

		