number = int(input())
sum_num = 0
sum_hero = 0
for i in range(1, number+1):
    sum_num += i
for i in range(1, number):
    hero = int(input())
    sum_hero += hero
print(sum_num-sum_hero)