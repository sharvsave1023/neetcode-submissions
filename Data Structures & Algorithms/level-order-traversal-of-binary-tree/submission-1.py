# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # final result
        q = collections.deque() # use queue to implement BFW
        q.append(root) # start with the root

        while q: # while something needs to be processed
            lenQ = len(q) #length of the level
            level = [] #appender to final result
            for i in range(lenQ): #from 0 to n
                node = q.popleft() #the current node
                if node: 
                    level.append(node.val) #add node to level
                    q.append(node.left) # process node's kids
                    q.append(node.right)
            if level: # only add if the level has something
                res.append(level)

        return res