# Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)
## Maximum Depth of Binary Tree 

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0

```
## Binary Tree Inorder Traversal 

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            if root.left:
                left = self.inorderTraversal(root.left)
            else: left = []
            if root.right:
                right = self.inorderTraversal(root.right)
            else: right = []
        else: return []
        return left + [root.val] + right
```
## Invert Binary Tree 

https://leetcode.com/problems/invert-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
```
## Binary Search Tree Iterator 

https://leetcode.com/problems/binary-search-tree-iterator/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorderTraversal(root: TreeNode) -> List[int]:
    if root:
        if root.left:
            left = inorderTraversal(root.left)
        else: left = []
        if root.right:
            right = inorderTraversal(root.right)
        else: right = []
    else: return []
    return left + [root.val] + right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = inorderTraversal(self.root)


    def next(self) -> int:
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        return True if self.stack else False

```
## Binary Tree Level Order Traversal 

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, level):
            if not node:
                return
            if len(self.result) <= level:
                self.result.append([])
            self.result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        self.result = []
        dfs(root, 0)
        return self.result
```
## Kth Smallest Element in a BST 

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array = []
        while True:
            while root:
                array.append(root)
                root = root.left
            root = array.pop()
            k = k - 1
            if not k:
                return root.val
            root = root.right
```
## Validate Binary Search Tree 

https://leetcode.com/problems/validate-binary-search-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)
        self.prev = -math.inf
        return inorder(root)
```
## Symmetric Tree 

https://leetcode.com/problems/symmetric-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def Zer(treel, treer):
            if not treel or not treer:
                return treer == treel
            if treel.val != treer.val:
                return False
            return Zer(treel.left, treer.right) and Zer(treel.right, treer.left)

        return Zer(root.left, root.right)
```
