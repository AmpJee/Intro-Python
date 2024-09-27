number = int(input())
num_list = list(map(int, input().split()))
count_neg = 0
count_pos = 0
for i in range(0,len(num_list)-1):
    if (num_list[i] < 0 and num_list[i+1] < 0) or (num_list[i] > 0 and num_list[i+1] > 0):
        print("YES")
        exit()
print("NO")