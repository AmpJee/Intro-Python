number = int(input())
num_list = list(map(int, input().split()))
answer = []
count_num = 0
for i in range(0,len(num_list)):
    if num_list[i] not in answer:
        answer.append(num_list[i])
        count_num += 1
print(count_num)