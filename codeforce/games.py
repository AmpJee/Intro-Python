text = input()
count_a = 0
count_b = 0
for i in text:
    if i == 'A':
        count_a += 1
    else:
        count_b += 1
if count_a > count_b:
    print("ALICE")
elif count_a < count_b:
    print("BOB")
else:
    print("DRAW")
