n = int(input().strip())

room_list = []
result = []

for i in range(n):
    st_inp, fn_inp = list(map(int, input().split()))
    room_list.append((st_inp, fn_inp))

# 빨리 끝나는 회의를 시간 순서대로 배열

# 회의 시작 시간에 따른 배열
room_list.sort(key = lambda room:room[0])
# 회의 끝나는 시간에 따른 배열
room_list.sort(key = lambda room:room[1])

# print(room_list)

min_fn_time = float('inf')
# min_fn_time = 100001
# min_idx = -1

for i in range(n):
    fin_time = room_list[i][1]
    if fin_time < min_fn_time:
        min_fn_time = fin_time
        min_idx = i

last_end_time = 0
for i in range(min_idx, n):
    st = room_list[i][0]
    fn = room_list[i][1]
    #현재 미팅의 시작 시간이 이전 미팅의 끝시간보다 늦을 때, 미팅의 수 증가 
    if st >= last_end_time:
        result.append(room_list[i])
        # meet_count+=1
        last_end_time = fn

# print(result)
print(len(result))