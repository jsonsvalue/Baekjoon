import sys
sys.setrecursionlimit(10**4)
tree = {}

def build_tree(preorder):
    if not preorder:
        return None
    
    root = preorder[0]
    tree[root] = { 'left': None, 'right' : None } 

    left_subtree = [ele for ele in preorder[1:] if ele < root]
    # print(left_subtree)
    right_subtree = [ele for ele in preorder[1:] if ele > root]
    # print(right_subtree)
    
    if left_subtree:
        tree[root]['left'] = build_tree(left_subtree)
    if right_subtree:
        tree[root]['right'] = build_tree(right_subtree)

    # print(root)
    return root

def postorder_trav(node):
    if node is None:
        return []
    
    left = tree[node]['left']
    right = tree[node]['right']

    return postorder_trav(left) + postorder_trav(right) + [node]



# def read_input():
#     preorder_list = []

#     while True:
#         ele = int(input())
#         if ele == "":
#             break
    
#         preorder_list.append(ele)

#     return preorder_list

# preorder_list = read_input()

# preorder_list = list(map(int, input().split()))


preorder_list = []

while True:
    try:
        x = int(input())
        preorder_list.append(x)
    except:
        break


# n = int(input())

# for i in range(n):
#     inp = int(input())
#     preorder_list.append(inp)

root = build_tree(preorder_list)

#print(tree)

postorder_list = postorder_trav(root)

for i in range(len(postorder_list)):
    print(postorder_list[i])

# print(*postorder_list, end = "\n")
# print(' '.join(map(str,postorder_list)))
# print(' '.join(str(x) for x in postorder_list))    


