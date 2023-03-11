class Node:
    def __init__(self,key):
        self.key = key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
#given a non empty binary
#search tree,return th enode
#with minimum key value
def minValueNode(node):  #right subtree
    current=node
    #loop down to find the leftmost leaf
    while(current.left is not None):
        current=current.left
    return current
#given a binary search tree and a key,this function
#delete the key and returns the new root
def deleteNode(root,key):
    #base case
    if root is None:
        return root
    #key<root,it lies in left subtree
    if key<root.key:
        root.left=deleteNode(root.left, key)
    elif (key>root.key):
        root.right = deleteNode(root.right, key)
    #if key is same as root's key
    #to be deleted
    else:
        #node with only one child or no child
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root = None
            return temp
        #node with two children
        #get the inorder successor
        #(smallest in the  right subtree)
        temp=minValueNode(root.right)
        #copy the inorder successor's content to  this node
        root.key=temp.key
        #deletew the inorder successor
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root, 50)
root=insert(root, 30)
root=insert(root, 20)
root=insert(root, 40)
root=insert(root, 70)
root=insert(root, 80)
print("inorder traversal of the given tree")
inorder(root)
print("\nDelete 20")
root=deleteNode(root,20)
print("inorder traversal of the modified tree")
inorder(root)
print("\nDelete 30")
root=deleteNode(root,30)
print("inorder traversal of the modified tree")
inorder(root)
print("\nDelete 50")
root=deleteNode(root,50)
print("inorder traversal of the modified tree")
inorder(root)
