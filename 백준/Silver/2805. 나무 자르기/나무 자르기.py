import sys
read = sys.stdin.readline

n, goal_sum = map(int, read().strip().split())
tree_list = list(map(int ,read().strip().split()))
# tree_list.sort()


start_cutt = 1 
end_cutt = max(tree_list)


while start_cutt <= end_cutt:
    mid_cutt = (start_cutt + end_cutt)//2
    tree_sum = 0
    for i in range(len(tree_list)):
        if tree_list[i] >= mid_cutt:
            tree_sum += tree_list[i] - mid_cutt
    
    if tree_sum >= goal_sum:
        start_cutt = mid_cutt + 1
    
    else:
        end_cutt = mid_cutt - 1


print(end_cutt)
    
