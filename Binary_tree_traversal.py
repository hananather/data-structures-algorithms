# definitio for a binary tree node
class TreeNode(object):
	def __init__(self, val =0, left = None, right = None):
		self.val = val
		self.left = left
		self.right =right

class Solution(object):
	def preorderTraversal(self, root):
		"""
		Given the root node of a binary tree return the pre-order traversal
		:type root: Treenode
		:rtype: List[int]
		"""
		def dfs(node):
			if not node:
				return
			result.append(node.val)
			dfs(node.left)
			dfs.node(node.right)

		result = []
		dfs(root)
		return result