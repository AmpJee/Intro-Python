number = int(input())
num_list = list(map(int, input().split()))
answer = []
for i in range(0,len(num_list)):
    if i % 2 != 1:
        answer.append(num_list[i])
print(*answer)