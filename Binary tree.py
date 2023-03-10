class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)
node1.leftchild=node2
node1.rightchild=node3
node2.leftchild=node4
node2.rightchild=node5
node3.leftchild=node6
node3.rightchild=node7
print("root node is")
print(node1.data)
print("left child of the node is :")
print(node1.leftchild.data)
print("right child of the node is :")
print(node1.rightchild.data)
print("node is:")
print(node2.data)
print("node is:")
print((node7.data))
