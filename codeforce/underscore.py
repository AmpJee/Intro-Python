text = input()
output = ""
for i, character in enumerate(text):
    output += character
    if i != len(text)-1:
        output += "_"
print(output)