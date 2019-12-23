# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#用root来记录当前想访问的节点，用stack记录访问轨迹，用result记录树的输出顺序
#基本思路就是：如果当前访问的点左数存在就压栈继续访问，如果不存在，就输出当前栈最上的元素，然后再访问其右点
#while的终止条件这块判断要注意
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if root == None:
            return result
        stack.append(root)
        root = root.left

        while stack != [] or root != None:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                result.append(temp.val)
                root = temp.right

        return result


if __name__ == "__main__":
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)
    s = Solution()
    result = s.inorderTraversal(t)
    print(result)