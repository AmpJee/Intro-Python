text_even = input()
letter = input()
output = ""
for i, character in enumerate(text_even):
    if i == len(text_even) / 2:
        output += letter
    output += character
print(output)