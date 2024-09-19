text = input()
index = len(text)-1
flag = True
for i, character in enumerate(text):
    if text[index - i] != text[i]:
        flag = False
        break
if flag == False :
    print("NO")
else:
    print("YES")