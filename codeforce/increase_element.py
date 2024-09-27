number = int(input())
num_list = list(map(int, input().split()))
increase = int(input())
for i in range(0,len(num_list)):
    num_list[i] += increase
print(*num_list)