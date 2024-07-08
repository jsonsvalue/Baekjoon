# 병합정렬(Merge Sort)
#.데이터의 수와 시간 복잡도를 고려한 코드를 작성해야 해

def merge_sort(num_list):
    if len(num_list)<=1:
        return num_list
    
    mid = len(num_list) // 2

    left_half = merge_sort(num_list[:mid])
    right_half = merge_sort(num_list[mid:])

    return merge_list(left_half, right_half)

def merge_list(left_list, right_list):
    sorted_list = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_list) and right_idx < len(right_list):
        
        if left_list[left_idx] < right_list[right_idx]:
            sorted_list.append(left_list[left_idx])
            left_idx += 1

        else:
            sorted_list.append(right_list[right_idx])
            right_idx += 1

    sorted_list.extend(left_list[left_idx:])
    sorted_list.extend(right_list[right_idx:])

    return sorted_list

n = int(input())
num_list = [int(input()) for i in range(n)]

sorted_list = merge_sort(num_list)

print(*sorted_list, sep = "\n")


    