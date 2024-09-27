number = int(input())
num_list = list(map(int, input().split()))
answer = []
for i in range(0,len(num_list)):
    if num_list[i] % 2 == 0:
        answer.append(num_list[i])
print(*answer)