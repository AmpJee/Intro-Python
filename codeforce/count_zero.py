number = int(input())
count_zero = 0
for i in range(number):
    value = int(input())
    if value == 0:
        count_zero += 1
print(count_zero)