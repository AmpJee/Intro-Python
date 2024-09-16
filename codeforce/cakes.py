apple_cakes = int(input())
orange_cakes = int(input())
first_bag = int(input())
second_bag = int(input())
if (min(apple_cakes, orange_cakes) <= min(first_bag, second_bag)) and max(apple_cakes, orange_cakes) <= max(first_bag, second_bag):
    print("YES")
else:
    print("NO")