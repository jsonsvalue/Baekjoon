n = int(input())

tree = {}
for i in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)
    

def preorder(start):
    if start != '.':
        print(start, end= "")
        preorder(tree[start][0])
        preorder(tree[start][1])
    



def inorder(start):
    if start !='.':
        inorder(tree[start][0])
        print(start, end = "")
        inorder(tree[start][1])


def postorder(start):
    if start!= '.':
        postorder(tree[start][0])
        postorder(tree[start][1])
        print(start, end = "")



preorder('A')
print()

inorder('A')
print()

postorder('A')
print()