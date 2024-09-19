text_even = input()
index = len(text_even) // 2
output = text_even[index:] + text_even[:index]
print(output)