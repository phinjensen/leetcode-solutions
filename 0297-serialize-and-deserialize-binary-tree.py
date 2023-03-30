# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        return f"{root.val}[{self.serialize(root.left)},{self.serialize(root.right)}]"

    def deserialize(self, data, depth=0):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        first_lb = data.index("[")
        node = TreeNode(int(data[:first_lb]))
        i = first_lb + 1
        lb = 0
        comma = -1
        end = -1
        while end == -1 and comma == -1:
            if comma == -1 and data[i] == "," and lb == 0:
                comma = i
            elif end == -1 and data[i] == "]" and lb == 0:
                end = i
            elif data[i] == "[":
                lb += 1
            elif data[i] == "]":
                lb -= 1
            i += 1
        node.left = self.deserialize(data[first_lb+1:comma], depth + 1)
        node.right = self.deserialize(data[comma+1:end], depth + 1)
        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

r = TreeNode(10)
r.left = TreeNode(20)
r.right = TreeNode(30)
r.left.left = TreeNode(40)
r.left.right = TreeNode(50)

ser = Codec()
#print(ser.serialize(r))
print(ser.deserialize(ser.serialize(r)))
